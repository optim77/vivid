from rich.console import Console

from scanner.username.instagram import instagram
from scanner.username.reddit import reddit
from scanner.username.facebook import facebook
from scanner.username.youtube import youtube
from scanner.username.pinterest import pinterest

async def scanner(domains: [str] = None) -> None:
    console = Console()
    if domains:
        pass
    else:
        #await instagram.scan("dupa154321312fdsffafdve2")
        console.print("[bold green]Facebook[/bold green]" if await facebook.check("ola") else "[bold red]Facebook[/bold red]")
        console.print("[bold green]Reddit[/bold green]" if await reddit.check("ola") else "[bold red]Reddit[/bold red]")

        #await youtube.check("dupa154321312fdsffafdve2")
        #await pinterest.check("santisr0610")