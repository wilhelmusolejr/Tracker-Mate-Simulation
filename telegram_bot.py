import asyncio
import os

from telegram import Bot
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get values from .env
TOKEN = "7649581310:AAG9flCCYC_odicG3TqhgQZfpbwmskm7mv4"
CHAT_ID = "1559668342"

async def send_telegram_notification(message):
    """Send a notification to Telegram asynchronously"""
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message) 

def notify_user(message):
    """Synchronous wrapper for async function"""
    asyncio.run(send_telegram_notification(message))  

# Test the function
if __name__ == "__main__":
    notify_user("User has started the application.")
