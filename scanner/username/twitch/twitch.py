from scanner.username.const import TWITCH_URL, TWITCH_TEXT
from scanner.username.verify import scan


async def check(username:str) -> bool:
    return await scan(username, TWITCH_URL, TWITCH_TEXT)