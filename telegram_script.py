import asyncio
import logging
import time

from telegram import Bot
from telegram.constants import ParseMode

from pynput.keyboard import Controller, Key
from pynput.mouse import Controller as MouseController, Button
import time

keyboard = Controller()
mouse = MouseController()

initial_waiting_time = 2
ready_location = [730, 430]

print("Move to the game in " + str(initial_waiting_time) +" seconds")
time.sleep(initial_waiting_time)

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

                
                last_message_id = latest_message.message_id  # Update last message ID
                last_text = latest_message.text.lower()  # Get latest message text

                print(f"Latest message: {last_text}")

                if last_text == "waiting":
                    mouse.position = (ready_location[0], ready_location[1])
                    mouse.click(Button.left, 1)
                    print("Pressed ready button")
                elif last_text == "ingame":    
                    print("Game started - Running in-game actions")
                    
                    start_time = time.time()
                    duration = 50  # Run for 30 seconds
                    
                    spam_key = 'w'  # Start with 's'
                    switch_time = time.time() + 5  # Switch every 5 seconds

                    while time.time() - start_time < duration:  # Run for 30 seconds
                        keyboard.press(spam_key)  # Press the current spam key
                        keyboard.release(spam_key)
                        print(f"Pressed {spam_key} key")

                        time.sleep(0.1)  # Adjust spam speed

                          # Switch between 's' and 'd' every 2 seconds
                        if time.time() >= switch_time:
                            spam_key = 'a' if spam_key == 'w' else 'w'  # Toggle between 's' and 'd'
                            switch_time = time.time() + 2  # Reset switch time

                    print("Loop ended after 50 seconds")

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
