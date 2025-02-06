import re
import asyncio
import cloudscraper
from scanner.username.const import HEADERS

async def scan(username: str, domain: str, text_verify: str = None, verify_by_http_code: bool = False) -> bool:
    """
    :param username: username to check
    :param domain: domain to check
    :param text_verify: text in return when no user
    :return: exist state
    """
    scraper = cloudscraper.create_scraper(browser={
        "browser": "chrome",
        "platform": "windows",
    })
    res = await asyncio.to_thread(scraper.get, domain + username, headers=HEADERS)

    if not text_verify and verify_by_http_code is True and res.status_code == 404:
        return False
    elif text_verify:
        return verify(text_verify, res.text)
    else: return True

def verify(text_verify: str, text: str) -> bool:
    """
    :param text: html content
    :param text_verify: text in return when no user
    :return: no account text existence
    """
    return False if re.search(text_verify, text) else True