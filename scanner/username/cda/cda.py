from typing import Dict

from scanner.username.const import CDA_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": CDA_URL + username,
            "result": await scan(username, CDA_URL, verify_by_http_code=True)
        }