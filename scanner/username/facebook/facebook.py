from scanner.username.verify import scan
from scanner.username.const import FACEBOOK_URL, FACEBOOK_TEXT


async def check(username: str) -> bool:
    return await scan(username, FACEBOOK_URL, FACEBOOK_TEXT)