from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext

TOKEN = "7652072253:AAGlvJ2UNtQNousCQF1Ld8MncU6GicxkRSU"

# Store the last received message
last_message = None

async def handle_message(update: Update, context: CallbackContext):
    global last_message
    last_message = update.message.text  # Store the last message
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
