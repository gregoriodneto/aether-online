from dataclasses import asdict

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, field_validator

from ..application import GameServer
from ..domain import (
    MAX_USERNAME_LENGTH,
    MIN_USERNAME_LENGTH,
    PlayerAlreadyConnected,
    ServerFull,
    strip_username,
)


class PlayerConnect(BaseModel):
    username: str = Field(min_length=MIN_USERNAME_LENGTH, max_length=MAX_USERNAME_LENGTH)

    @field_validator("username", mode="before")
    @classmethod
    def validate_username(cls, value: object) -> str:
        return strip_username(value)


def create_router(server: GameServer) -> APIRouter:
    router = APIRouter()

    @router.get("/health")
    def get_health():
        return {"status": server.get_health()}

    @router.get("/server/status")
    def get_server_status():
        return asdict(server.get_status())

    @router.post("/players/connect", status_code=201)
    def post_players_connect(player: PlayerConnect):
        try:
            username = server.connect_player(player.username)
        except PlayerAlreadyConnected as error:
            raise HTTPException(status_code=409, detail="Player already connected") from error
        except ServerFull as error:
            raise HTTPException(status_code=503, detail="Server is full") from error

        return {"message": "Player connected", "username": username}

    return router
