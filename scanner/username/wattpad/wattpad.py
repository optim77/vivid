from scanner.username.const import WATTPAD_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": WATTPAD_URL + username,
            "result": await scan(username, WATTPAD_URL, verify_by_http_code=True, http_code=404)
        }