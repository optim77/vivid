from scanner.username.const import TELEGRAM_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": TELEGRAM_URL + username,
            "result": await scan(username, TELEGRAM_URL, verify_by_http_code=True, http_code=302)
        }