from scanner.username.const import WORDPRESS_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": WORDPRESS_URL + username,
            "result": await scan(username, WORDPRESS_URL, verify_by_http_code=True, http_code=404)
        }