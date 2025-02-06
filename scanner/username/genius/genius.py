

from scanner.username.const import GENIUS_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
        "url": GENIUS_URL + username,
        "result": await scan(username, GENIUS_URL, verify_by_http_code=True)
    }