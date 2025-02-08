from typing import Dict

from scanner.username.const import MEDIUM_URL, MEDIUM_TEXT
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": MEDIUM_URL + username,
            "result": await scan(username, MEDIUM_URL, MEDIUM_TEXT)
        }