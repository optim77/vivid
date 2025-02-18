from scanner.username.const import TRADINGVIEW_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": TRADINGVIEW_URL + username,
            "result": await scan(username, TRADINGVIEW_URL, verify_by_http_code=True, http_code=404)
        }