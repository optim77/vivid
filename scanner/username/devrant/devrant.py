from scanner.username.const import DEVRANT_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": DEVRANT_URL + username,
            "result": await scan(username, DEVRANT_URL, verify_by_http_code=True, http_code=302)
        }