import httpx
from rich.console import Console


async def fuzzer(domain: str, use_proxy: bool, proxy: str = None):
    console = Console()
    with open('fuzzer/url_fuzzer_list.txt', 'r') as f:
        endpoint = f.readlines()
        for e in endpoint:
            print(e)
            e = e.replace('\n', '').replace('/', '')
            async with httpx.AsyncClient() as client:
                client.headers.update({'User-Agent': 'Mozilla/5.0'})
                res = await client.get(f'https://{domain}/{e}')
                color = "green" if res.status_code != 404 else "red"
                console.print(f"[bold {color}]https://{domain}/{e} {res.status_code}[/bold {color}]")
                if res.status_code != 404:
                    console.print(res.status_code)
