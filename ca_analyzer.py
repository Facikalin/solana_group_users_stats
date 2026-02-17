import re
from datetime import datetime, timedelta, timezone
from collections import defaultdict

SOLANA_CA_REGEX = re.compile(r'\b[1-9A-HJ-NP-Za-km-z]{32,44}\b')

async def analyze_last_month(client, group):
    now = datetime.now(timezone.utc)
    one_month_ago = now - timedelta(days=30)

    user_token_map = defaultdict(set)
    user_message_count = defaultdict(int)

    print("\nSon 1 ay mesajları analiz ediliyor...")

    async for message in client.iter_messages(group, offset_date=one_month_ago):
        if not message.text or not message.sender_id:
            continue

        matches = SOLANA_CA_REGEX.findall(message.text)

        if matches:
            sender = message.sender_id
            user_message_count[sender] += 1

            for ca in matches:
                user_token_map[sender].add(ca)

    return user_token_map, user_message_count
