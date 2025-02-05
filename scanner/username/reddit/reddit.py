from scanner.username.verify import scan
from scanner.username.const import REDDIT_URL, REDDIT_TEXT


async def check(username: str) -> bool:
    return await scan(username, REDDIT_URL, REDDIT_TEXT)