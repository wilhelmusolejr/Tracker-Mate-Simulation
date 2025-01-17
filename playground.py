import asyncio
import logging
import time
from telegram import Bot
from telegram.constants import ParseMode

# Telegram Bot Token
TOKEN = "7652072253:AAGlvJ2UNtQNousCQF1Ld8MncU6GicxkRSU"

# Initialize bot
bot = Bot(token=TOKEN)

# Store last processed message ID to prevent duplicates
last_message_id = 0


async def check_latest_message():
    """Fetches the latest message every minute and processes it."""
    global last_message_id

    while True:
        try:
            updates = await bot.get_updates(offset=-1)  # Get latest update
            if updates:
                latest_message = updates[-1].message

                if latest_message and latest_message.message_id != last_message_id:
                    last_message_id = latest_message.message_id  # Update last message ID
                    last_text = latest_message.text.lower()  # Get latest message text

                    print(f"Latest message: {last_text}")

                    if last_text == "waiting":
                        print("Action: Pressed ready button")
                    elif last_text == "ingame":
                        print("Game started - Running in-game actions")

            await asyncio.sleep(60)  # Wait for 1 minute before checking again

        except Exception as e:
            logging.error(f"Error fetching updates: {e}")
            await asyncio.sleep(10)  # Wait 10 seconds before retrying


async def main():
    """Main function to run the bot."""
    print("Bot is running... checking for messages every 1 minute.")
    await check_latest_message()


if __name__ == "__main__":
    asyncio.run(main())
