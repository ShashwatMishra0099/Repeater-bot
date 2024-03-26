import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.environ.get('7112203931:AAFPtXa60Q5wPyUF9JO3MzhnHJUwSNzZdvU"')

# Define the default message and repetition count
DEFAULT_MESSAGE = "Hello, world!"
DEFAULT_COUNT = 3

def start(update, context):
    update.message.reply_text('Welcome to the Message Repeater Bot!')

def repeat(update, context):
    message = context.args[0] if context.args else DEFAULT_MESSAGE
    count = int(context.args[1]) if len(context.args) > 1 else DEFAULT_COUNT
    
    # Repeat the message the specified number of times
    for _ in range(count):
        update.message.reply_text(message)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("repeat", repeat))

    # Start the Bot
    PORT = int(os.environ.get('PORT', '8443'))
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path="7112203931:AAFPtXa60Q5wPyUF9JO3MzhnHJUwSNzZdvU")
    updater.bot.set_webhook("https://git.heroku.com/messagerepeater.git7112203931:AAFPtXa60Q5wPyUF9JO3MzhnHJUwSNzZdvU")

    updater.idle()

if __name__ == '__main__':
    main()
