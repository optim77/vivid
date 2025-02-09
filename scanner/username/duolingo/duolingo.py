from scanner.username.const import DUOLINGO_URL, DUOLINGO_TEXT
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": DUOLINGO_URL + username,
            "result": await scan(username, DUOLINGO_URL, DUOLINGO_TEXT)
        }