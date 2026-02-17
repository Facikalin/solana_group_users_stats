async def list_groups(client):
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


async def select_group(client):
    groups = await list_groups(client)

    choice = int(input("\nAnaliz etmek istediğin grubun numarasını gir: "))
    selected_group = groups[choice - 1]

    print(f"\nSeçilen Grup: {selected_group.name}")
    return selected_group
