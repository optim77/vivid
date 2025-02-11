from scanner.username.const import BUZZFEED_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": BUZZFEED_URL + username,
            "result": await scan(username, BUZZFEED_URL, verify_by_http_code=True, http_code=404)
        }