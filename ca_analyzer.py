import re
from datetime import datetime, timedelta, timezone
from collections import defaultdict

SOLANA_CA_REGEX = re.compile(r'\b[1-9A-HJ-NP-Za-km-z]{32,44}\b')
MAX_CA_PER_MESSAGE = 3  # Bot spam filtre

async def analyze_last_week(client, group):
    now = datetime.now(timezone.utc)
    one_week_ago = now - timedelta(days=7)

    token_data = {}

    print("\nSon 1 hafta mesajları analiz ediliyor...")

    async for message in client.iter_messages(group, offset_date=one_week_ago):

        if not message.text:
            continue

        matches = SOLANA_CA_REGEX.findall(message.text)

        if not matches:
            continue

        if len(matches) > MAX_CA_PER_MESSAGE:
            continue

        sender = await message.get_sender()
        if not sender:
            continue

        username = sender.username if sender.username else sender.first_name

        for ca in matches:

            if ca not in token_data:
                token_data[ca] = {
                    "first_seen": message.date,
                    "callers": set([username])
                }
            else:
                token_data[ca]["callers"].add(username)

    return token_data
