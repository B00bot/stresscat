# -*- coding: utf-8 -*-
import requests
import config
import telebot
from telebot import types
from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters
import os
import logging
import random
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(config.token)
dispatcher = updater.dispatcher

bot = telebot.TeleBot(config.token)

#стикеры для randint
stickers = ["CAADAgADCwADlp-MDpuVH3sws_a7FgQ", "CAADAgAD7g0AAqgILwj_8DhBu2dnDRYE", "CAADBAADfQADzjkIDSgZQLclD7jiFgQ", "CAADBAADRAADzjkIDbv4-ULKD6hiFgQ", "CAADAgAD0gIAArnzlwt4AXAE0tVijhYE", "CAADAgAD2gEAAsdjXBUX3pc5V_GYDBYE", "CAADBAADmAADzjkIDRaa2RCZbCJWFgQ", "CAADBAADkwADzjkIDYydFNXPYxHoFgQ", "CAADAgAD4w0AAqgILwh6UH_uBQWn_RYE", "CAADAgADBAgAAhhC7ghzMDDTpZ3HjRYE", "CAADAgADCAADl_TGFHTucAABYtoR1BYE"]

###################################################################################################################################
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Привет, если хочешь узнать тайну, отправь /secret Если нужны доказательства - отправь /proof Если грустно - отправь /grustno")	
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def secret(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Мой создатель любит тебя")
secret_handler = CommandHandler('secret', secret)
dispatcher.add_handler(secret_handler)

def help(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Если хочешь узнать тайну, отправь /secret Если нужны доказательства - отправь /proof Если грустно - отправь /grustno")	
help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

def proof(bot, update):
    randomstick=random.randint(0,10)
    pic=stickers[randomstick]
    bot.sendMessage(chat_id=update.message.chat_id, text="Создатель просил передать...")
    bot.sendSticker(chat_id=update.message.chat_id, sticker=pic);
proof_handler = CommandHandler('proof', proof)
dispatcher.add_handler(proof_handler)

def grustno(bot, update):
    pic=open('s1200.jpeg', 'rb')
    bot.send_photo(chat_id=update.message.chat_id, photo=pic);
    bot.sendMessage(chat_id=update.message.chat_id, text="Ни грустииии")
grustno_handler = CommandHandler('grustno', grustno)
dispatcher.add_handler(grustno_handler)
##################################################################################################################################
#MENU
##################################################################################################################################
def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu
button_list = [
    KeyboardButton("Секрет", callback_data=secret),
    KeyboardButton("Доказательство", callback_data=proof),
    KeyboardButton("Грустнаа", callback_data=grustno)
    KeyboardButton("Памагити", callback_data='/help')
]
reply_markup = ReplyKeyboardMarkup(util.build_menu(button_list, n_cols=2))
bot.send_message(..., "A two-column menu", reply_markup=reply_markup)
###################################################################################################################################

#ставим вебхук
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=config.token)
updater.bot.set_webhook("https://stresscatbot.herokuapp.com/" + config.token)

