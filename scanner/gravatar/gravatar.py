import hashlib
import requests
from rich.console import Console


def gravatar(email):
    console = Console()
    hash_email = hashlib.md5(email.strip().lower().encode()).hexdigest()
    url = f"https://www.gravatar.com/avatar/{hash_email}?d=404"
    response = requests.get(url)
    return console.print(f'[bold green]Email registered at gravatar {url} [/bold green]')  \
        if  response.status_code == 200 \
        else console.print(f'[bold red]Email not registered at gravatar {url} [/bold red]')
