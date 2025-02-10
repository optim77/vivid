from scanner.username.const import DEVIANTART_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": DEVIANTART_URL + username,
            "result": await scan(username, DEVIANTART_URL, verify_by_http_code=True, http_code=404)
        }