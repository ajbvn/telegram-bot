import telegram
from telegram.ext import Updater, CommandHandler
from random import randint

TOKEN = "addyourtokenhere"
bot = telegram.Bot(TOKEN)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

def roll(bot, update):
    num = randint(1, 6)
    update.message.reply_text(str(num))

roll_handler = CommandHandler('roll', roll)
dispatcher.add_handler(roll_handler)

updater.start_polling()
