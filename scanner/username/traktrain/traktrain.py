from scanner.username.const import TRACKTRAIN_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": TRACKTRAIN_URL + username,
            "result": await scan(username, TRACKTRAIN_URL, verify_by_http_code=True, http_code=302)
        }