import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.environ.get('7112203931:AAFPtXa60Q5wPyUF9JO3MzhnHJUwSNzZdvU')

def start(update, context):
    update.message.reply_text('Welcome to the Message Repeater Bot!')

def repeat(update, context):
    # Get the message and number of times to repeat
    text = ' '.join(context.args)
    try:
        count = int(context.args[0])
        message = ' '.join(context.args[1:])
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /repeat <count> <message>')
        return
    
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
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.set_webhook("https://your-heroku-app.herokuapp.com/" + TOKEN)

    updater.idle()

if __name__ == '__main__':
    main()
