import django
import os


from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import *
from products.models import *

API_KEY = '1916496543:AAFTF6muwjLySqBiL3WIamhzkQ615xf0luo'
print('Bot started')

def handle_message(update , context:CallbackContext):
    text=str(update.message.text).lower()
    print(update)

    update.message.reply_text( f"Hi, {update['message']['chat']['first_name']},please select one option:\n Stupid \n Fat \n Stupid:")


if __name__ == '__main__':
    updater = Updater(API_KEY, use_context =True)
    dp =updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text , handle_message))

    updater.start_polling(1.0)
    updater.idle()