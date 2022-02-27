from telegram.ext import *
#from telegram import *      #for inlinekeyboard

from bot_logic import bot_logic

user_bot = {}

def start_cmd(update, context):
    user_bot[str(update.effective_chat.id)] = bot_logic()
    update.message.reply_photo('https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_thumbnail_photos/001/850/940/datas/medium.png',
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

def handle_msg(update, context):
    response = user_bot[str(update.effective_chat.id)].respond(update.message.text)
    update.message.reply_text(response)

def error(update, context):
    print(f"Error: {context.error}\n {update}")
    update.message.reply_text('Oh no...something bad happened. bot_brain.exe not working')
    update.message.reply_text('Why not try /start again?')

def main():
    with open("token.key", 'r') as token:
        BOT_TOKEN = token.read()
    
    updater = Updater(BOT_TOKEN, use_context=True)
    dpc = updater.dispatcher

    dpc.add_handler(CommandHandler("start", start_cmd))
    dpc.add_handler(CommandHandler("help", help_cmd))
    dpc.add_handler(CommandHandler("format", result_format_cmd))
    
    dpc.add_handler(MessageHandler(Filters.text, handle_msg))
    
    dpc.add_error_handler(error)
    
    start(updater)
    
def start(updater):
    updater.start_polling()
    print("Commence Bot Operations...")
    
    updater.idle()


if __name__ == "__main__":
    main()