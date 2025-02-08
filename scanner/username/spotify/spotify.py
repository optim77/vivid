from typing import Dict

from scanner.username.const import SPOTIFY_URL, SPOTIFY_TEXT
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
        "url": SPOTIFY_URL + username,
        "result": await scan(username, SPOTIFY_URL, SPOTIFY_TEXT)
    }