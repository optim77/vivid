from scanner.username.const import KWEJK_URL
from scanner.username.verify import scan


async def check(username:str) -> bool:
    return await scan(username, KWEJK_URL, verify_by_http_code=True)