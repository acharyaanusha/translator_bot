from telegram.ext import Updater, MessageHandler, CommandHandler, Filters


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    print('Received /start command')
    update.message.reply_text('Hi!I am a translater. Give me a word in english and I shall give the equivalent in kannada')


def help(bot, update):
    print('Received /help command')
    update.message.reply_text('Help!')


def echo(bot, update):
    my_dic={'sleep':'nidde','eat':'tinnu','drink':'kudi'}
    print('Received an update')
    if update.message.text.lower() in my_dic.keys():
       answer= my_dic[update.message.text.lower()]
       update.message.reply_text(answer)
    else:
       update.message.reply_text("key not in dictionary")

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("515850760:AAGjN106zbtr-hRj8Qm7rU0BQOqMvQJiQ1s")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
