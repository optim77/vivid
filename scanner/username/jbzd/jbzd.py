from scanner.username.const import JBZD_URL
from scanner.username.verify import scan


async def check(username:str) -> bool:
    return await scan(username, JBZD_URL, verify_by_http_code=True)