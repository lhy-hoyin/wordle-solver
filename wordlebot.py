from telegram.ext import *
#from telegram import *      #for inlinekeyboard

from bot_logic import bot_logic

user_bot = {}

def start_cmd(update, context):
    user_bot[str(update.effective_chat.id)] = bot_logic()
    update.message.reply_text('Hello, did you need help with Wordle?')
    # TODO: add inline keyboard for Yes and Exit button

def help_cmd(update, context):
    update.message.reply_text('Ask google for help, we only had 24 hours for this XD')

def result_format_cmd(update, context):
    update.message.reply_text(user_bot[str(update.effective_chat.id)].result_format_message_str())
    
def restart_cmd(update, context):
    update.message.reply_text(user_bot[str(update.effective_chat.id)].restart())

def handle_msg(update, context):
    response = user_bot[str(update.effective_chat.id)].respond(update.message.text)
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
    dpc.add_handler(CommandHandler("format", result_format_cmd))
    dpc.add_handler(CommandHandler("restart", restart_cmd))
    
    dpc.add_handler(MessageHandler(Filters.text, handle_msg))
    
    dpc.add_error_handler(error)
    
    updater.start_polling()
    print("Commence Bot Operations...")
    
    updater.idle()


if __name__ == "__main__":
    main()