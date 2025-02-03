from scanner.username.verify import scan
from scanner.username.const import FACEBOOK_URL, FACEBOOK_TEXT


async def check(username: str) -> bool:
    """
    :param username: facebook username
    :return: exist state
    """
    return await scan(username, FACEBOOK_URL, FACEBOOK_TEXT)