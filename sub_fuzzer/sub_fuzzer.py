import csv
import random

import dns.resolver
import concurrent.futures
from rich.console import Console

def load_subdomains(filename):
    console = Console()
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        console.print(f"[bold red] File {filename} not found.[/bold red]")
        return []

def load_proxies(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"[bold red] File {filename} not found.[/bold red]")
        return []

def check_subdomain(domain, sub, use_proxy, proxies, results):
    full_domain = f"{sub}.{domain}"
    proxy_used = None

    if use_proxy and proxies:
        proxy_used = random.choice(proxies)
        print(f"[*] Używanie proxy: {proxy_used}")

    try:
        resolver = dns.resolver.Resolver()

        if use_proxy:
            resolver.nameservers = ["1.1.1.1"]

        resolver.resolve(full_domain, "A")
        print(f"[bold green] Found: {full_domain}[/bold green]")
        results.append((full_domain, "Found", proxy_used))
    except dns.resolver.NXDOMAIN:
        print(f"[bold red] Not exists: {full_domain}[/bold red]")
    except dns.resolver.NoAnswer:
        print(f"[bold red] Brak odpowiedzi dla: {full_domain}[/bold red]")
    except dns.exception.Timeout:
        print(f"[bold red] Timeout: {full_domain}[/bold red]")


def run_fuzzer(domain, use_proxy=False, export_csv=False):
    proxies = load_proxies("proxies.txt") if use_proxy else []
    results = []
    subdomains = load_subdomains("subdomains.txt")
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(domain, check_subdomain, sub, use_proxy, proxies, results) for sub in subdomains]
        concurrent.futures.wait(futures)

    if export_csv:
        with open("sub_domain_results.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Subdomain", "Status", "Proxy"])
            writer.writerows(results)
        print("[bold green] Saved to results.csv[/bold green]")
