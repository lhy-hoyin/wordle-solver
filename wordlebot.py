from telegram.ext import *
#from telegram import *      #for inlinekeyboard
import teleKey as key
import responseTest as R

print("Commence Bot Operations...")

def start_cmd(update, context):
    update.message.reply_text('Hello, did you need help with Wordle?')
    #add Inline keyboard for Yes and Exit button

def help_cmd(update, context):
    update.message.reply_text('Ask google for help, we only had 24 hours for this')

def handle_msg(update, context):
    text = str(update.message.text).lower()

    response = R.sample_responses(text)
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(key.API_Key, use_context=True)
    dpc = updater.dispatcher

    dpc.add_handler(CommandHandler("start", start_cmd))
    dpc.add_handler(CommandHandler("help", help_cmd))

    dpc.add_handler(MessageHandler(Filters.text, handle_msg))

    dpc.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()