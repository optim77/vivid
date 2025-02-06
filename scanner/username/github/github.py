from scanner.username.const import GITHUB_URL
from scanner.username.verify import scan


async def check(username:str) -> bool:
    return await scan(username, GITHUB_URL, verify_by_http_code=True)