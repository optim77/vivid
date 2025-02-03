import re
import cloudscraper
import asyncio
from scanner.username.const import INSTAGRAM_URL

# TODO: not working this way, need to implement other, e.g. selenium
async def scan(username:str) -> bool:
    scraper = cloudscraper.create_scraper()
    res = await asyncio.to_thread(scraper.get, INSTAGRAM_URL + username)
    return verify(res.text)

def verify(text: str) -> bool:
    return True if re.search("This content isn't available right now", text) else False