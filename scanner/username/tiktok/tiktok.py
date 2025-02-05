from scanner.username.const import TIKTOK_URL, TIKTOK_TEXT
from scanner.username.tiktok.scrapper import scrapper
from scanner.username.verify import scan


async def check(username:str) -> bool:
    return await scrapper(TIKTOK_URL + username)