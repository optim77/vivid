from scanner.username.const import WYKOP_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": WYKOP_URL + username,
            "result": await scan(username, WYKOP_URL, verify_by_http_code=True, http_code=404)
        }