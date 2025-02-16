from scanner.username.const import STRAVA_URL
from scanner.username.verify import scan


async def check(username:str) -> dict[str, bool]:
    return {
            "url": STRAVA_URL + username,
            "result": await scan(username, STRAVA_URL, verify_by_http_code=True, http_code=302)
        }