import csv
import random

import dns.resolver
import concurrent.futures

from rich.console import Console
console = Console()

def load_subdomains(filename):
    try:
        with open(f'sub_fuzzer/{filename}', "r") as file:
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

def format_domain(domain, sub):
    if 'http://' in domain:
        domain = domain.split('http://')
        return f'http://{sub}.{domain[1]}'
    if 'https://' in domain:
        domain = domain.split('https://')
        return f'https://{sub}.{domain[1]}'
    if 'www.' in domain:
        domain = domain.split('www.')
        return f'www.{sub}.{domain[1]}'

def check_subdomain(domain, sub, use_proxy, proxies, results):
    full_domain = format_domain(domain, sub)
    print(full_domain)
    proxy_used = None

    if use_proxy and proxies:
        proxy_used = random.choice(proxies)
        print(f"[bold green] Use proxy: {proxy_used}[/bold green]")

    try:
        resolver = dns.resolver.Resolver()

        if use_proxy:
            resolver.nameservers = ["1.1.1.1"]

        resolver.resolve(full_domain, "A")
        console.print(f"[bold green] Found: {full_domain}[/bold green]")
        results.append((full_domain, "Found", proxy_used))
    except dns.resolver.NXDOMAIN:
        console.print(f"[bold red] Not exists: {full_domain}[/bold red]")
    except dns.resolver.NoAnswer:
        console.print(f"[bold red] No answer for: {full_domain}[/bold red]")
    except dns.exception.Timeout:
        console.print(f"[bold red] Timeout: {full_domain}[/bold red]")


def run_fuzzer(domain, use_proxy=False, export_csv=False):
    proxies = load_proxies("proxies.txt") if use_proxy else []
    results = []
    subdomains = load_subdomains("subdomains.txt")
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_subdomain, domain, sub, use_proxy, proxies, results) for sub in subdomains]
        concurrent.futures.wait(futures)

    if export_csv:
        with open("sub_domain_results.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Subdomain", "Status", "Proxy"])
            writer.writerows(results)
        console.print("[bold green] Saved to results.csv[/bold green]")
