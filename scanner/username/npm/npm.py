from scanner.username.const import NPM_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": NPM_URL + username,
            "result": await scan(username, NPM_URL, verify_by_http_code=True, http_code=404)
        }