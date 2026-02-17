import asyncio
from group_selector import select_group

async def main():
    selected_group = await select_group()

if __name__ == "__main__":
    asyncio.run(main())