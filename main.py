import asyncio
from telegram_client import get_client
from group_selector import select_group
from ca_analyzer import analyze_last_week

async def main():
    async with get_client() as client:
        group = await select_group(client)

        token_data = await analyze_last_week(client, group)

        print("\n=== Son 1 Hafta Token Analizi ===\n")

        sorted_tokens = sorted(token_data.items(), key=lambda x: x[1]["first_seen"])

        for ca, data in sorted_tokens[:20]:
            print(f"CA: {ca}")
            print(f"İlk Paylaşım: {data['first_seen']}")
            print(f"Callers: {', '.join(data['callers'])}")
            print("-" * 60)

        print(f"\nToplam Benzersiz Token (1 Hafta): {len(token_data)}")

if __name__ == "__main__":
    asyncio.run(main())
