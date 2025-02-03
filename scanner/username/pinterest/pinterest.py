from scanner.username.verify import scan
from scanner.username.const import PINTEREST_URL, PINTEREST_TEXT

async def check(username: str):
    """
    :param username: pinterest username
    :return:
    """
    return await scan(username, PINTEREST_URL, PINTEREST_TEXT)