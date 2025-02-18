from scanner.username.const import TRAKT_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": TRAKT_URL + username,
            "result": await scan(username, TRAKT_URL, verify_by_http_code=True, http_code=404)
        }