import re
import asyncio
import cloudscraper
from scanner.username.const import HEADERS

async def scan(username: str, domain: str, text_verify: str) -> bool:
    """
    :param username: username to check
    :param domain: domain to check
    :param text_verify: text in return when no user
    :return: exist state
    """
    scraper = cloudscraper.create_scraper()
    res = await asyncio.to_thread(scraper.get, domain + username, headers=HEADERS)
    return verify(text_verify, res.text)

def verify(text_verify: str, text: str) -> bool:
    """
    :param text: html content
    :param text_verify: text in return when no user
    :return: no account text existence
    """
    return True if re.search(text_verify, text) else False