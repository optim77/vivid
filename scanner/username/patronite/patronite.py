from scanner.username.const import PATRONITE_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": PATRONITE_URL + username,
            "result": await scan(username, PATRONITE_URL, verify_by_http_code=True, http_code=404)
        }