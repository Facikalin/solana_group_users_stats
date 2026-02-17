import asyncio
from telegram_client import get_client

async def list_groups():
    async with get_client() as client:
        dialogs = await client.get_dialogs()

        groups = []
        index = 1

        print("\nÜye Olduğun Gruplar:\n")

        for dialog in dialogs:
            if dialog.is_group or dialog.is_channel:
                print(f"{index}. {dialog.name}")
                groups.append(dialog)
                index += 1

        return groups


async def select_group():
    groups = await list_groups()

    choice = int(input("\nAnaliz etmek istediğin grubun numarasını gir: "))
    selected_group = groups[choice - 1]

    print(f"\nSeçilen Grup: {selected_group.name}")
    return selected_group
