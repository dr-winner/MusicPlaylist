from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class Song(BaseModel):
    title: str
    artist: str
    duration: str


playlist: List[Song] = []


@app.get("/playlist", response_model=List[Song])
def get_playlist():
    return playlist


@app.post("/playlist", response_model=List[Song])
def add_song(song: Song):
    playlist.append(song)
    return playlist


@app.delete("/playlist/{index}", response_model=List[Song])
def remove_song(index: int):
    if 0 <= index < len(playlist):
        playlist.pop(index)
        return playlist
    else:
        raise HTTPException(status_code=404, detail="Song not found")


@app.put("/playlist/{index}", response_model=List[Song])
def edit_song(index: int, song: Song):
    if 0 <= index < len(playlist):
        playlist[index] = song
        return playlist
    else:
        raise HTTPException(status_code=404, detail="Song not found")
