import asyncio
import csv

from rich.console import Console
from selenium.webdriver.common.devtools.v85.runtime import await_promise

from scanner.username.buzzfeed import buzzfeed
from scanner.username.clubhouse import clubhouse
from scanner.username.codewars import codewars
from scanner.username.cracked import cracked
from scanner.username.deviantart import deviantart
from scanner.username.fiverr import fiverr
from scanner.username.genius import genius
from scanner.username.github import github
from scanner.username.hackersploit import hackersploit
from scanner.username.huggingface import huggingface
from scanner.username.instagram import instagram
from scanner.username.leetcode import leetcode
from scanner.username.npm import npm
from scanner.username.patronite import patronite
from scanner.username.reddit import reddit
from scanner.username.facebook import facebook
from scanner.username.snapchat import snapchat
from scanner.username.tradingview import tradingview
from scanner.username.trakt import trakt
from scanner.username.twitch import twitch
from scanner.username.unsplash import unsplash
from scanner.username.vimeo import vimeo
from scanner.username.wattpad import wattpad
from scanner.username.wordpress import wordpress
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
from scanner.username.tryhackme import tryhackme
from scanner.username.devrant import devrant
from scanner.username.aboutme import aboutme

async def scanner(username: [str] = None, csv_output: bool = False) -> None:
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
        #"Buzzfeed": buzzfeed.check,
        #"Codewars": codewars.check,
        #"Hackersploit": hackersploit.check,
        #"Snapchat": snapchat.check,
        #"Tradingview": tradingview.check,
        #"Trakt": trakt.check,
        #"Tryhackme": tryhackme.check,
        #"Unsplash": unsplash.check,
        "Vimeo": vimeo.check,
        "NPM": npm.check,
        "Wordpress": wordpress.check,
        "Devrant": devrant.check,
        "About me": aboutme.check




        # TODO: add these:
        # https://www.g2a.com/pl/user/
        # https://0x00sec.org/u/
        # https://trello.com/u/ola


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
        # "Cracked": cracked.check,
    }

    tasks = {name: asyncio.create_task(func(username)) for name, func in services.items()}
    results = await asyncio.gather(*tasks.values())
    output_data = []


    for (name, result) in zip(tasks.keys(), results):
        color = "green" if result['result'] else "red"
        console.print(f"[bold {color}]{name} {result['url']}[/bold {color}]")

        if csv_output:
            output_data.append([name, result['url'], result['result']])

    if csv_output and output_data:
        with open("username_scanner_results.csv", mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Service", "URL", "Exists"])
            writer.writerows(output_data)
        console.print(f"[bold blue]Results saved to username_scanner_results.csv[/bold blue]")

# loop = asyncio.get_running_loop()
# with ThreadPoolExecutor(max_workers=3) as executor:
#     tasks = [loop.run_in_executor(executor, selenium_task, url) for url in urls]
#     results = await asyncio.gather(*tasks)
# return results
