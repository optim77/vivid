from scanner.username.const import UNSPLASH_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": UNSPLASH_URL + username,
            "result": await scan(username, UNSPLASH_URL, verify_by_http_code=True, http_code=404)
        }