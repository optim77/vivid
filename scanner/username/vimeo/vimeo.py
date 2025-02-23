from scanner.username.const import VIMEO_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": VIMEO_URL + username,
            "result": await scan(username, VIMEO_URL, verify_by_http_code=True, http_code=404)
        }