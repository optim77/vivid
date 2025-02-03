import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

async def driver(url):
    options = Options()
    #options.add_argument('--headless')
    #options.add_argument("--disable-gpu")

    wd = webdriver.Chrome(options=options)
    wd.get(url)

    time.sleep(200)
