import asyncio
import cloudscraper

from scanner.driver import driver
from scanner.username.const import YOUTUBE_URL, HEADERS

# TODO: need to use selenium
async def check(username: str) -> bool:
    await driver(YOUTUBE_URL + username)
