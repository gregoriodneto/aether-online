from unittest import TestCase

from fastapi.testclient import TestClient

from app.adapters.memory import InMemoryConnectedPlayers
from app.application import GameServer
from app.main import create_app


class GameServerHttpTests(TestCase):
    def test_health(self):
        with TestClient(create_app()) as client:
            response = client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "healthy"})

    def test_server_status(self):
        with TestClient(create_app()) as client:
            response = client.get("/server/status")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "server": "Aether Online",
                "status": "online",
                "players_online": 0,
                "max_players": 100,
            },
        )

    def test_connect_player_updates_server_status(self):
        with TestClient(create_app()) as client:
            response = client.post("/players/connect", json={"username": " Alice "})
            status = client.get("/server/status")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json(), {"message": "Player connected", "username": "Alice"}
        )
        self.assertEqual(status.status_code, 200)
        self.assertEqual(status.json()["players_online"], 1)

    def test_connect_player_handles_duplicate_and_full_server(self):
        server = GameServer(InMemoryConnectedPlayers(), max_players=1)
        with TestClient(create_app(server)) as client:
            connected = client.post("/players/connect", json={"username": "Alice"})
            duplicate = client.post("/players/connect", json={"username": "Alice"})
            full = client.post("/players/connect", json={"username": "Bobby"})

        self.assertEqual(connected.status_code, 201)
        self.assertEqual(duplicate.status_code, 409)
        self.assertEqual(duplicate.json(), {"detail": "Player already connected"})
        self.assertEqual(full.status_code, 503)
        self.assertEqual(full.json(), {"detail": "Server is full"})
