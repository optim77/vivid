from scanner.username.const import STEAM_URL, STEAM_TEXT
from scanner.username.verify import scan


async def check(username:str) -> bool:
    return await scan(username, STEAM_URL, STEAM_TEXT,)