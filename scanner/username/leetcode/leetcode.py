from scanner.username.const import LEETCODE_URL, LEETCODE_TEXT
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": LEETCODE_URL + username,
            "result": await scan(username, LEETCODE_URL, LEETCODE_TEXT)
        }