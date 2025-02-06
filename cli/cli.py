import argparse
from rich.console import Console
from scanner.username.scanner import scanner



async def cli():
    console = Console()
    intro = """
    [bold green]
    ██╗   ██╗██╗██╗   ██╗██╗██████╗ 
    ██║   ██║██║██║   ██║██║██╔══██╗
    ██║   ██║██║██║   ██║██║██║  ██║
    ╚██╗ ██╔╝██║╚██╗ ██╔╝██║██║  ██║
     ╚████╔╝ ██║ ╚████╔╝ ██║██████╔╝
      ╚═══╝  ╚═╝  ╚═══╝  ╚═╝╚═════╝ 
                                
    Welecome to vivid!
    [/bold green]
    """
    parser = argparse.ArgumentParser(description="Welcome to vivid")
    parser.add_argument("-u", type=str, nargs="?", help="Username to check")
    parser.add_argument("-e", type=str, nargs="?", help="Email to check")
    parser.add_argument("-d", type=str, nargs="+", help="Domain to validate a single domain (e.g., gmail) or a collection (e.g., gmail, amazon)")
    parser.add_argument("-l", action="store_true", help="List available domains")
    args = parser.parse_args()

    console.print(intro)
    await scanner("ola312xrx23r2")
    if args.l:
        console.print("List of available domains:")
        return

    if not args.e or not args.u:
        console.print("Error: Email or username parameter is required unless using")
        parser.print_help()
        return

    #if args.u:

    #console.print(f"Inserted mail: {args.email}")

    # if not is_email(args.email):
    #     console.print("[bold red]Error: Email is invalid[/bold red]")

