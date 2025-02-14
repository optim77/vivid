from scanner.username.const import HACKERSPLOIT_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": HACKERSPLOIT_URL + username,
            "result": await scan(username, HACKERSPLOIT_URL, verify_by_http_code=True, http_code=404)
        }