from scanner.username.const import ABOUT_ME_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": ABOUT_ME_URL + username,
            "result": await scan(username, ABOUT_ME_URL, verify_by_http_code=True, http_code=404)
        }