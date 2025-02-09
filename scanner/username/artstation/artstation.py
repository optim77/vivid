from scanner.username.const import ARTSTATION_URL, ARTSTATION_TEXT
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": ARTSTATION_URL + username,
            "result": await scan(username, ARTSTATION_URL, ARTSTATION_TEXT)
        }