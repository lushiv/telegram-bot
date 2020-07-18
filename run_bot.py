from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, Updater, CommandHandler, MessageHandler, CallbackQueryHandler,Filters
from config import BotConfig
from crypto_price import get_cms_data
updater = Updater(BotConfig.token_id, use_context=True)
dispatcher = updater.dispatcher

print('*'*40)
print('CryptoCurrency Price Bot  is running')
print('*'*40)


def welcomeMessage(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Hello Welcome Type CryptoCurrency id \n btc = bitcoin , ltc = litecoin ")


# all crypto price 
def textHandle(update: Update, context: CallbackContext):
    print(update)
    text = update.message.text

    print(text)
    if text.startswith(""):
        coin = text.upper()
        print(coin)
        if get_cms_data(coin) is not None:
            context.bot.send_message(chat_id=update.message.chat_id,
                                     text="1 {} = {} USD".format(coin, get_cms_data(coin)))
        else:
            context.bot.send_message(chat_id=update.message.chat_id,
                                     text="Please provide correct coin symbol")

def main():
    dispatcher.add_handler(CommandHandler('start', welcomeMessage))
    dispatcher.add_handler(MessageHandler(Filters.text, textHandle))

    
if __name__ == '__main__':
    try:
        main()
        updater.start_polling()
        updater.idle()

    except KeyboardInterrupt:
        exit()
