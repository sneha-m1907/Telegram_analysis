
   
from telethon.sync import TelegramClient
import pandas as pd

# Your API credentials
api_id = '25565526'
api_hash = '99a6442eccecb37a07e908fe79a498a1'
phone_number = '+919902810910'
session_name = 'scrape'

client = TelegramClient(session_name, api_id, api_hash)

async def scrape_telegram_data(channel_name):
    messages = await client.get_messages(channel_name, limit=500)
    data = []
    for message in messages:
        data.append({
            'sender_id': message.sender_id,
            'text': message.text,
            'date': message.date
        })
    df = pd.DataFrame(data)
    df.to_csv(f'{channel_name}_messages.csv', index=False)  # Save to CSV
    print(f"Saved messages to {channel_name}_messages.csv")

with client:
   client.loop.run_until_complete(scrape_telegram_data('Investing'))

