from scanner.username.const import CRACKED_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": CRACKED_URL + username,
            "result": await scan(username, CRACKED_URL, verify_by_http_code=True, http_code=302)
        }