# solana_group_users_stats

A Python project to collect and analyze user statistics from Solana-related Telegram groups.

## Project Structure

- main.py: Entry point for the application.
- telegram_client.py: Handles Telegram API interactions.
- group_selector.py: Logic for selecting and managing Telegram groups.
- user_stats.py: Functions for collecting and analyzing user statistics.
- config.py: Configuration settings (API keys, group IDs, etc.).
- requirements.txt: Python dependencies.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure your API keys and settings in config.py.
3. Run the main script:
   ```bash
   python main.py
   ```

## Notes
- Ensure you comply with Telegram's terms of service when using their API.
- Replace placeholder values in config.py with your actual credentials.
