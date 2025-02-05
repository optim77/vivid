from selenium.webdriver.common.by import By
from scanner.driver import create_driver


async def scrapper(address: str):
    wd = create_driver()
    wd.get(address)
    try:
        is_exist = wd.find_element(By.XPATH, "//p[contains(text(), 'Looking for videos? Try browsing our trending creators, hashtags, and sounds.')]")
        return False if is_exist else True
    except:
        return False