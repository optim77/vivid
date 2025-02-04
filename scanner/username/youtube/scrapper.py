from selenium.webdriver.common.by import By
from scanner.driver import create_driver


async def scrapper(address: str):
    wd = create_driver()
    wd.get(address)
    wd.find_elements(By.XPATH, "//form")[1].click()
    is_exist = wd.find_elements(By.CLASS_NAME, "yt-spec-touch-feedback-shape__fill")
    return True if is_exist else False