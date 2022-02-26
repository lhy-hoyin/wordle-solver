from telegram.ext import *
#from telegram import *      #for inlinekeyboard

from bot_logic import bot_respond

def start_cmd(update, context):
    update.message.reply_text('Hello, did you need help with Wordle?')
    # TODO: add inline keyboard for Yes and Exit button

def help_cmd(update, context):
    update.message.reply_text('Ask google for help, we only had 24 hours for this')

def handle_msg(update, context):
    response = bot_respond(update.message.text)
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    with open("token.key", 'r') as token:
        BOT_TOKEN = token.read()
    
    updater = Updater(BOT_TOKEN, use_context=True)
    dpc = updater.dispatcher

    dpc.add_handler(CommandHandler("start", start_cmd))
    dpc.add_handler(CommandHandler("help", help_cmd))
    
    dpc.add_handler(MessageHandler(Filters.text, handle_msg))
    
    dpc.add_error_handler(error)
    
    updater.start_polling()
    print("Commence Bot Operations...")
    
    updater.idle()


if __name__ == "__main__":
    main()