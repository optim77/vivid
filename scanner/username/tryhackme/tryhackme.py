from scanner.username.const import TRYHACKME_URL, TRYHACKME_TEXT
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": TRYHACKME_URL + username,
            "result": await scan(username, TRYHACKME_URL, text_verify=TRYHACKME_TEXT)
        }