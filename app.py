from pynput.keyboard import Controller, Key
from pynput.mouse import Controller as MouseController, Button
import time

from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext

TOKEN = "7652072253:AAGlvJ2UNtQNousCQF1Ld8MncU6GicxkRSU"
initial_message = "waiting"
last_message = None

keyboard = Controller()
mouse = MouseController()

initial_waiting_time = 3
ready_location = [730, 430]

print("Move to the game in " + str(initial_waiting_time) +" seconds")
time.sleep(initial_waiting_time)

async def handle_message(update: Update, context: CallbackContext):
    global last_message
    
    last_message = update.message.text  # Store the last message
    
    if(last_message == "waiting"):
      print("waiting")
      # mouse.position = (ready_location[0], ready_location[1])
      # mouse.click(Button.left, 1)
      # print("Pressed ready button")
      # time.sleep(10)
  
    if(last_message == "ingame"):
      print("Game is starting")
      # spam_key = 'w'  # Start with 's'
      # switch_time = time.time() + 5  # Switch every 5 seconds

      # while True:
      #     keyboard.press(spam_key)  # Press the current spam key
      #     keyboard.release(spam_key)
      #     print(f"Pressed {spam_key} key")

      #     time.sleep(0.1)  # Adjust spam speed

      #     # Switch between 's' and 'd' every 2 seconds
      #     if time.time() >= switch_time:
      #         spam_key = 'a' if spam_key == 'w' else 'w'  # Toggle between 's' and 'd'
      #         switch_time = time.time() + 2  # Reset switch time
    print(f"Last message received: {last_message}")

    await update.message.reply_text(f"Last message stored!")

async def get_last_message(update: Update, context: CallbackContext):
    if last_message:
        await update.message.reply_text(f"Last message: {last_message}")
    else:
        await update.message.reply_text("No messages received yet.")

def main():
    app = Application.builder().token(TOKEN).build()

    # Handle all text messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Command to retrieve the last message
    app.add_handler(MessageHandler(filters.Command(["last"]), get_last_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()


# CODE BY TC.666