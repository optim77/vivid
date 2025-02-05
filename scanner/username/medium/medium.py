from scanner.username.const import MEDIUM_URL, MEDIUM_TEXT
from scanner.username.verify import scan


async def check(username:str) -> bool:
    return await scan(username, MEDIUM_URL, MEDIUM_TEXT)