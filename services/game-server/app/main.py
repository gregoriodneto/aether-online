from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator

app = FastAPI(title="Aether Online Game Server")

MAX_PLAYERS = 100
players = set()

class PlayerConnect(BaseModel):
    username: str = Field(min_length=3, max_length=30)
    
    @field_validator("username", mode="before")
    @classmethod
    def validate_username(cls, value):
        if not isinstance(value, str):
            raise ValueError("Username must be a string")
        return value.strip()

@app.get("/health")
def get_health():
    return {"status": "healthy"}

@app.get("/server/status")
def get_server_status():
    return {
        "server": "Aether Online",
        "status": "online",
        "players_online": len(players),
        "max_players": MAX_PLAYERS
    }

@app.post("/players/connect", status_code=201)
def post_players_connect(player: PlayerConnect):
    if player.username in players:
        raise HTTPException(
            status_code=409,
            detail="Player already connected"
        )
        
    if len(players) >= MAX_PLAYERS:
        raise HTTPException(
            status_code=503,
            detail="Server is full"
        )
            
    players.add(player.username)
    return {
        "message": "Player connected",
        "username": player.username
    }