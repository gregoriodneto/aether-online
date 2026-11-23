from fastapi import FastAPI

from .adapters.http import create_router
from .adapters.memory import InMemoryConnectedPlayers
from .application import GameServer


def create_app(server: GameServer | None = None) -> FastAPI:
    if server is None:
        server = GameServer(InMemoryConnectedPlayers())

    app = FastAPI(title="Aether Online Game Server")
    app.include_router(create_router(server))
    return app


app = create_app()