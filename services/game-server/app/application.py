from dataclasses import dataclass
from typing import Protocol

from .domain import MAX_USERNAME_LENGTH, MIN_USERNAME_LENGTH, strip_username


class ConnectedPlayers(Protocol):
    def connect(self, username: str, max_players: int) -> None:
        """Register a player atomically or raise PlayerAlreadyConnected or ServerFull."""
        ...

    def count(self) -> int: ...


@dataclass(frozen=True)
class ServerStatus:
    server: str
    status: str
    players_online: int
    max_players: int


class GameServer:
    def __init__(self, players: ConnectedPlayers, max_players: int = 100) -> None:
        self._players = players
        self._max_players = max_players

    def get_health(self) -> str:
        return "healthy"

    def get_status(self) -> ServerStatus:
        return ServerStatus(
            server="Aether Online",
            status="online",
            players_online=self._players.count(),
            max_players=self._max_players,
        )

    def connect_player(self, username: str) -> str:
        username = strip_username(username)
        if not MIN_USERNAME_LENGTH <= len(username) <= MAX_USERNAME_LENGTH:
            raise ValueError(
                f"Username must be between {MIN_USERNAME_LENGTH} "
                f"and {MAX_USERNAME_LENGTH} characters"
            )
        self._players.connect(username, self._max_players)
        return username
