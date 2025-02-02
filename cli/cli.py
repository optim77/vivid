import argparse
from rich.console import Console
from utils.validation import is_email
def cli():
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
    parser.add_argument("email", type=str, nargs="?", help="Email to check")
    parser.add_argument("-d", type=str, nargs="+", help="Domain to validate a single domain (e.g., gmail) or a collection (e.g., gmail, amazon)")
    parser.add_argument("-l", action="store_true", help="List available domains")
    args = parser.parse_args()

    if args.l:
        console.print("List of available domains:")
        return

    if not args.email:
        console.print("Error: Email is required unless using '-l'")
        parser.print_help()
        return

    console.print(intro)
    console.print(f"Inserted mail: {args.email}")

    if not is_email(args.email):
        console.print("[bold red]Error: Email is invalid[/bold red]")

