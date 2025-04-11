import hashlib
import requests
from rich.console import Console

from utils.load_proxy import load_proxy


def gravatar(email, use_proxy=False):
    console = Console()
    proxies = []
    if use_proxy:
        proxies = load_proxy()
    hash_email = hashlib.md5(email.strip().lower().encode()).hexdigest()
    url = f"https://www.gravatar.com/avatar/{hash_email}?d=404"
    response = requests.get(url, proxies=proxies)
    return console.print(f'[bold green]Email registered at gravatar {url} [/bold green]')  \
        if  response.status_code == 200 \
        else console.print(f'[bold red]Email not registered at gravatar {url} [/bold red]')
