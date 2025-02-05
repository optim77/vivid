from time import sleep

from selenium.webdriver.common.by import By
from scanner.driver import create_driver


async def scrapper(address: str, text_verify):
    wd = create_driver()
    wd.get(address)
    sleep(123)
    # try:
    wd.find_element(By.XPATH, "//span[contains(text(), 'Allow all cookies')]").click()
    wd.find_element(By.XPATH, "//aria-label[contains(text(), 'Close')]").click()
    is_exist = wd.find_element(By.XPATH, "//span[contains(text(), 'This content isn't available right now')]")
    return False if is_exist else True
# except:
#    return False
