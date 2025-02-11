from scanner.username.const import CLUBHOUSE_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": CLUBHOUSE_URL + username,
            "result": await scan(username, CLUBHOUSE_URL, verify_by_http_code=True, http_code=404)
        }