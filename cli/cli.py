import argparse
from rich.console import Console

from scanner.gravatar.gravatar import gravatar
from scanner.username.scanner import scanner
import pkgutil

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
    parser.add_argument("-csv", action="store_true", help="Export result to csv file")
    parser.add_argument("-gravatar", type=str, nargs="?", help="Check if hash created based on inserted mail")
    args = parser.parse_args()

    console.print(intro)

    #await scanner("ola")

    if args.l:
        console.print([module.name for module in pkgutil.iter_modules(scanner.username.__path__)])
        console.print("List of available domains:")
        return
    if args.gravatar:
        gravatar(args.gravatar)

    if  args.e == '' or args.u == '':
        console.print("Error: Email or username parameter is required unless using")
        parser.print_help()
        return

    if args.u:
        if args.csv:
            await scanner(args.u, csv_output=True)
        else:
            await scanner(args.u, csv_output=False)

    #console.print(f"Inserted mail: {args.email}")

    # if not is_email(args.email):
    #     console.print("[bold red]Error: Email is invalid[/bold red]")

