from scanner.username.const import HUGGINGFACE_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": HUGGINGFACE_URL + username,
            "result": await scan(username, HUGGINGFACE_URL, verify_by_http_code=True, http_code=404)
        }