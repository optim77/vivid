from scanner.username.const import CODEWARS_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": CODEWARS_URL + username,
            "result": await scan(username, CODEWARS_URL, verify_by_http_code=True, http_code=404)
        }