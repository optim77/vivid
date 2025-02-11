import asyncio
from rich.console import Console

from scanner.username.buzzfeed import buzzfeed
from scanner.username.clubhouse import clubhouse
from scanner.username.deviantart import deviantart
from scanner.username.fiverr import fiverr
from scanner.username.genius import genius
from scanner.username.github import github
from scanner.username.huggingface import huggingface
from scanner.username.instagram import instagram
from scanner.username.leetcode import leetcode
from scanner.username.patronite import patronite
from scanner.username.reddit import reddit
from scanner.username.facebook import facebook
from scanner.username.twitch import twitch
from scanner.username.wattpad import wattpad
from scanner.username.youtube import youtube
from scanner.username.pinterest import pinterest
from scanner.username.spotify import spotify
from scanner.username.steam import steam
from scanner.username.tiktok import tiktok
from scanner.username.medium import medium
from scanner.username.cda import cda
from scanner.username.kwejk import kwejk
from scanner.username.olx import olx
from scanner.username.nine_gag import ngag
from scanner.username.duolingo import duolingo
from scanner.username.artstation import artstation
from scanner.username.codepen import codepen

async def scanner(username: [str] = None) -> None:
    console = Console()

    services = {
        # Working good:
        #"Medium": medium.check
        #"Steam": steam.check,
        #"Spotify": spotify.check,
        #"Github": github.check,
        #"CDA": cda.check
        #"JBZD": cda.check,
        #"Kwejk": kwejk.check,
        #"Genius": genius.check,
        #"OLX": olx.check,
        #"9Gag": ngag.check,
        #"Wattpad": wattpad.check,
        #"Artstation": artstation.check,
        #"Patronite": patronite.check,
        #"Codepen": codepen.check,
        #"Huggingface": huggingface.check,
        #"Deviantart": deviantart.check,
        #"Clubhouse": clubhouse.check,
        "Buzzfeed": buzzfeed.check,



        # TODO: add these:
        # giphy
        # https://www.g2a.com/pl/user/
        # https://www.codewars.com/users/


        # Problematic
        # "Reddit": reddit.check,
        # "Facebook": facebook.check,
        # "TikTok": tiktok.check
        # "Twitch": twitch.check
        # "Instagram": instagram.check
        # "Pinterest": pinterest.check
        # "Duolingo": duolingo.check,
        # "Fiverr": fiverr.check
        # "Leetcode": leetcode.check,
    }

    tasks = {name: asyncio.create_task(func(username)) for name, func in services.items()}

    results = await asyncio.gather(*tasks.values())

    for (name, result) in zip(tasks.keys(), results):
        color = "green" if result['result'] else "red"
        console.print(f"[bold {color}]{name} {result['url']}[/bold {color}]")



# loop = asyncio.get_running_loop()
# with ThreadPoolExecutor(max_workers=3) as executor:  # Możesz dostosować liczbę wątków
#     tasks = [loop.run_in_executor(executor, selenium_task, url) for url in urls]
#     results = await asyncio.gather(*tasks)
# return results
