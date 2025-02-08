from scanner.username.const import NINE_GAG_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": NINE_GAG_URL + username,
            "result": await scan(username, NINE_GAG_URL, verify_by_http_code=True, http_code=404)
        }