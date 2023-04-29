import os
import telegram.ext as tele
from dotenv import load_dotenv   # pip install python-dotenv

#from telegram import *      #for inlinekeyboard

from .bot_logic import BotLogic

START_PHOTO_PATH = '../img/wordle-solver-light.jpg'
PORT = int(os.environ.get('PORT', 5000))

load_dotenv()
user_bot = {}

def get_telegram_bot_token():
    return os.getenv('TELEGRAM_BOT_TOKEN', 'MISSING_BOT_TOKEN')

def start_cmd(update, context):
    user_bot[str(update.effective_chat.id)] = BotLogic()
    update.message.reply_photo(
        photo=open(START_PHOTO_PATH, 'rb'),
        caption='Hi there ^u^, did you need help with Wordle?\nType the first word to get started!')
    update.message.reply_text("Feeling lost? See what to do at /help")
    # TODO: add inline keyboard for Yes and Exit button

def help_cmd(update, context):
    update.message.reply_text(
        "First time asking for help? No worries :) We are here to help!\n"
        "Start off with typing a word, then provided me with the result of the word like this:\n"
        "• 0: Wrong letter choice\n"
        "• 1: Correct letter position\n"
        "• 2: Wrong letter position\n"
        "Example: 10200\n"
        "Please provide the result in the correct /format\n"
        "I'll suggest some words to try then :) Feel free to try other words too."
    )

def result_format_cmd(update, context):
    update.message.reply_text(user_bot[str(update.effective_chat.id)].result_format_message_str())

def thanks_cmd(update, context):
    update.message.reply_text("On behalf of the programmers, you're welcome! :D")

def handle_msg(update, context):
    update.message.reply_text(user_bot[str(update.effective_chat.id)].respond(update.message.text))

def error(update, context):
    print(f"Error: {context.error}\n {update}")
    update.message.reply_text('Oh no...something bad happened. bot-brain.exe not working')
    update.message.reply_text('Why not try /start again?')

if __name__ == "__main__":
    main()
    
def main():
    # Retrieve telegram bot token
    BOT_TOKEN = get_telegram_bot_token()
    
    updater = tele.Updater(BOT_TOKEN, use_context=True)
    dpc = updater.dispatcher

    # CommandHandler
    dpc.add_handler(tele.CommandHandler("start", start_cmd))
    dpc.add_handler(tele.CommandHandler("help", help_cmd))
    dpc.add_handler(tele.CommandHandler("format", result_format_cmd))
    dpc.add_handler(tele.CommandHandler("thanks", thanks_cmd))

    # MessageHandler
    dpc.add_handler(tele.MessageHandler(tele.Filters.text, handle_msg))

    # Error Handler
    dpc.add_error_handler(error)
    
    # start bot
    start(updater)
    
    # wait for bot to stop
    updater.idle()
    on_stopping()
    
def start(updater):
    BOT_TOKEN = get_telegram_bot_token()
    env = os.getenv('RuntimeEnv', 'local')

    if env == 'local':
        print("Bot started polling ...")
        updater.start_polling()
        
    else:
        updater.start_webhook(
            listen="0.0.0.0",
            port=int(PORT),
            url_path = BOT_TOKEN,
            webhook_url = os.getenv('WEBHOOK_HOST') + "/api")
        print("Bot webhook started ...")

def on_stopping():
    print("Bot is stopping ...")

# https://api.telegram.org/bot{your_bot_token}/setWebhook?url={your_vercel_domain_url}/api/bot
#WEBHOOK_URL = urljoin(WEBHOOK_HOST, "/api/bot")
