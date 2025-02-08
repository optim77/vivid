from typing import Dict

from scanner.username.const import GITHUB_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
        "url": GITHUB_URL + username,
        "result": await scan(username, GITHUB_URL, verify_by_http_code=True)
    }