from scanner.username.const import YOUTUBE_URL
from scanner.username.youtube.scrapper import scrapper


async def check(username: str) -> bool:
    return await scrapper(YOUTUBE_URL + username)
