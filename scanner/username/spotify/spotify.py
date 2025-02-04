from scanner.username.const import SPOTIFY_URL, SPOTIFY_TEXT
from scanner.username.verify import scan


async def check(username:str) -> bool:
    return await scan(username, SPOTIFY_URL, SPOTIFY_TEXT)