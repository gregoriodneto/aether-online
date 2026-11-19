from threading import Lock

from ..domain import PlayerRoster


class InMemoryConnectedPlayers:
    def __init__(self) -> None:
        self._roster = PlayerRoster()
        self._lock = Lock()

    def connect(self, username: str, max_players: int) -> None:
        with self._lock:
            self._roster.connect(username, max_players)

    def count(self) -> int:
        with self._lock:
            return self._roster.count()
