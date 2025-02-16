from scanner.username.const import SNAPCHAT_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": SNAPCHAT_URL + username,
            "result": await scan(username, SNAPCHAT_URL, verify_by_http_code=True, http_code=404)
        }