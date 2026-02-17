import asyncio
from telegram_client import get_client
from group_selector import select_group
from ca_analyzer import analyze_last_month

async def main():
    async with get_client() as client:
        group = await select_group(client)

        user_token_map, user_message_count = await analyze_last_month(client, group)

        print("\n=== Son 1 Ay Call İstatistikleri ===\n")

        results = []

        for user in user_token_map:
            total_unique_tokens = len(user_token_map[user])
            total_messages = user_message_count[user]

            results.append((user, total_unique_tokens, total_messages))

        results.sort(key=lambda x: x[1], reverse=True)

        for user, unique_tokens, total_msgs in results[:20]:
            print(f"UserID: {user}")
            print(f"  Farklı Token: {unique_tokens}")
            print(f"  CA Mesaj Sayısı: {total_msgs}")
            print("-" * 40)

if __name__ == "__main__":
    asyncio.run(main())
