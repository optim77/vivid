from rich.console import Console

from scanner.username.instagram import instagram
from scanner.username.reddit import reddit
from scanner.username.facebook import facebook
from scanner.username.youtube import youtube
from scanner.username.pinterest import pinterest
from scanner.username.spotify import spotify
async def scanner(domains: [str] = None) -> None:
    console = Console()
    if domains:
        pass
    else:
        await spotify.check("asdxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        #await instagram.scan("dupa154321312fdsffafdve2")
        #console.print("[bold green]Facebook[/bold green]" if await facebook.check("ola") else "[bold red]Facebook[/bold red]")
        #console.print("[bold green]Reddit[/bold green]" if await reddit.check("ola") else "[bold red]Reddit[/bold red]")
        #console.print("[bold green]Reddit[/bold green]" if await youtube.check("ola") else "[bold red]Reddit[/bold red]")

        #await youtube.check("dupa154321312fdsffafdve2")
        #await pinterest.check("santisr0610")

        # loop = asyncio.get_running_loop()
        # with ThreadPoolExecutor(max_workers=3) as executor:  # Możesz dostosować liczbę wątków
        #     tasks = [loop.run_in_executor(executor, selenium_task, url) for url in urls]
        #     results = await asyncio.gather(*tasks)
        # return results