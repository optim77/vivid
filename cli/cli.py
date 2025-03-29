import argparse
from rich.console import Console

from fuzzer.fuzzer import fuzzer
from scanner.gravatar.gravatar import gravatar
from scanner.username.scanner import scanner
import pkgutil
from sub_fuzzer.sub_fuzzer import run_fuzzer
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
    parser.add_argument("-s", type=str, nargs="?", help="Domain to sub fuzzing")
    parser.add_argument("-p", action="store_true", default=False, help="Use inserted proxy")
    parser.add_argument("-d", type=str, nargs="+", help="Domain to validate a single domain (e.g., gmail) or a collection (e.g., gmail, amazon)")
    parser.add_argument("-l", action="store_true", help="List available domains")
    parser.add_argument("-csv", action="store_true", default=False, help="Export result to csv file")
    parser.add_argument("-gravatar", type=str, nargs="?", help="Check if hash created based on inserted mail")
    parser.add_argument("-f", type=str, nargs='?', help="Domain to fuzz")
    args = parser.parse_args()

    console.print(intro)

    #await scanner("ola")
    print(args.csv)

    if args.l:
        console.print([module.name for module in pkgutil.iter_modules(scanner.username.__path__)])
        console.print("List of available domains:")
        return
    if args.gravatar:
        gravatar(args.gravatar)

    if  args.e == '' or args.u == '' or args.f == '' or args.s == '':
        console.print("Error: Need to specify action and pass arguments")
        parser.print_help()
        return

    if args.u:
        await scanner(args.u, csv_output=args.csv)


    if args.f:
        await fuzzer(args.f, proxy=args.p, csv_output=args.csv)

    if args.s:
        run_fuzzer(args.s, use_proxy=args.p, export_csv=args.csv)

    #console.print(f"Inserted mail: {args.email}")

    # if not is_email(args.email):
    #     console.print("[bold red]Error: Email is invalid[/bold red]")

