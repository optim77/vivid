import asyncio
from rich.console import Console

from scanner.username.genius import genius
from scanner.username.github import github
from scanner.username.instagram import instagram
from scanner.username.reddit import reddit
from scanner.username.facebook import facebook
from scanner.username.twitch import twitch
from scanner.username.youtube import youtube
from scanner.username.pinterest import pinterest
from scanner.username.spotify import spotify
from scanner.username.steam import steam
from scanner.username.tiktok import tiktok
from scanner.username.medium import medium
from scanner.username.cda import cda
from scanner.username.kwejk import kwejk

async def scanner(username: [str] = None) -> None:
    console = Console()

    services = {
        #"Medium": medium.check
        #"Steam": steam.check,
        #"Spotify": spotify.check,
        #"Github": github.check,
        #"CDA": cda.check
        #"JBZD": cda.check,
        #"Kwejk": kwejk.check,
        "Genius": genius.check,



        # Problematic
        # "Reddit": reddit.check,
        # "Facebook": facebook.check,
        # "TikTok": tiktok.check
        # "Twitch": twitch.check
        # "Instagram": instagram.check
    }

    tasks = {name: asyncio.create_task(func(username)) for name, func in services.items()}

    results = await asyncio.gather(*tasks.values())

    for (name, result) in zip(tasks.keys(), results):
        color = "green" if result else "red"
        console.print(f"[bold {color}]{name}[/bold {color}]")



# loop = asyncio.get_running_loop()
# with ThreadPoolExecutor(max_workers=3) as executor:  # Możesz dostosować liczbę wątków
#     tasks = [loop.run_in_executor(executor, selenium_task, url) for url in urls]
#     results = await asyncio.gather(*tasks)
# return results
