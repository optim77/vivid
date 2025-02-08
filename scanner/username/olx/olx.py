from scanner.username.const import OLX_URL, OLX_TEXT
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": OLX_URL + username,
            "result": await scan(username, OLX_URL, OLX_TEXT)
        }