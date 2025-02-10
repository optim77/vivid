from scanner.username.const import CODEPEN_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": CODEPEN_URL + username,
            "result": await scan(username, CODEPEN_URL, verify_by_http_code=True, http_code=404)
        }