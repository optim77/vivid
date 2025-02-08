from typing import Dict

from scanner.username.const import STEAM_URL, STEAM_TEXT
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": STEAM_URL + username,
            "result": await scan(username, STEAM_URL, STEAM_TEXT)
        }