import csv

import httpx
from rich.console import Console
import random

async def fuzzer(domain: str, proxy: bool = False, csv_output=False):
    console = Console()
    output_data = []
    proxies = []
    if proxy:
        with open('../proxy.txt', 'r') as f:
            proxies = f.read().splitlines()
    with open('path_fuzzer/url_fuzzer_list.txt', 'r') as f:
        endpoint = f.readlines()
        for e in endpoint:
            e = e.replace('\n', '').replace('/', '')
            async with httpx.AsyncClient(proxy=random.choice(proxies)) as client:
                client.headers.update({'User-Agent': 'Mozilla/5.0'})
                res = await client.get(f'https://{domain}/{e}')
                color = "green" if res.status_code != 404 else "red"
                console.print(f"[bold {color}]https://{domain}/{e} {res.status_code}[/bold {color}]")
                output_data.append([e, res.status_code])

        if csv_output and output_data:
            with open("url_fuzzer_results.csv", mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["URL", "HTTP CODE"])
                writer.writerows(output_data)
            console.print(f"[bold blue]Results saved to url_fuzzer_results.csv[/bold blue]")
