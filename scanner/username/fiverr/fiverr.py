from scanner.username.const import FIVERR_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": FIVERR_URL + username,
            "result": await scan(username, FIVERR_URL, verify_by_http_code=True, http_code=404)
        }