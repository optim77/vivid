import asyncio
from cli import cli


async def main():
    await cli.cli()

if __name__ == "__main__":
    asyncio.run(main())

