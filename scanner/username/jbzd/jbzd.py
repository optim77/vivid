from typing import Dict

from scanner.username.const import JBZD_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": JBZD_URL + username,
            "result": await scan(username, JBZD_URL, verify_by_http_code=True)
        }