MIN_USERNAME_LENGTH = 3
MAX_USERNAME_LENGTH = 30

def strip_username(value: object) -> str:
    if not isinstance(value, str):
        raise ValueError("Username must be a string")
    return value.strip()

class PlayerAlreadyConnected(Exception):
    pass

class ServerFull(Exception):
    pass

class PlayerRoster:
    def __init__(self) -> None:
        self._usernames: set[str] = set()

    def connect(self, username: str, max_players: int) -> None:
        if username in self._usernames:
            raise PlayerAlreadyConnected
        if self.count() >= max_players:
            raise ServerFull
        self._usernames.add(username)

    def count(self) -> int:
        return len(self._usernames)
