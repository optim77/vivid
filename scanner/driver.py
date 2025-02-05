from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver():
    """
    :return: instance of selenium.webdriver.Chrome
    """
    options = {
        'request_headers': {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Referer": "https://google.com",
        }
    }
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {"intl.accept_languages": "en,en_US"})
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument("--disable-gpu")

    return webdriver.Chrome(seleniumwire_options=options, options=chrome_options)
