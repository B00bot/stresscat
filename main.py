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

markup = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/secret')
button2 = types.KeyboardButton('/proof')
button3 = types.KeyboardButton('/grustno')
button4 = types.KeyboardButton('/help')
markup.row(button1, button2, button3)
markup.row(button4)

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Привет, если хочешь узнать тайну, отправь /secret Если нужны доказательства - отправь /proof Если грустно - отправь /grustno", reply_markup=markup)	
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def secret(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Мой создатель любит тебя", reply_markup=markup)
secret_handler = CommandHandler('secret', secret)
dispatcher.add_handler(secret_handler)

def help(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Если хочешь узнать тайну, отправь /secret Если нужны доказательства - отправь /proof Если грустно - отправь /grustno", reply_markup=markup)	
help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

#стикеры для randint
stickers = ["CAADAgADCwADlp-MDpuVH3sws_a7FgQ", "CAADAgAD7g0AAqgILwj_8DhBu2dnDRYE", "CAADBAADfQADzjkIDSgZQLclD7jiFgQ", "CAADBAADRAADzjkIDbv4-ULKD6hiFgQ", "CAADAgAD0gIAArnzlwt4AXAE0tVijhYE", "CAADAgAD2gEAAsdjXBUX3pc5V_GYDBYE", "CAADBAADmAADzjkIDRaa2RCZbCJWFgQ", "CAADBAADkwADzjkIDYydFNXPYxHoFgQ", "CAADAgAD4w0AAqgILwh6UH_uBQWn_RYE", "CAADAgADBAgAAhhC7ghzMDDTpZ3HjRYE", "CAADAgADCAADl_TGFHTucAABYtoR1BYE"]

def proof(bot, update):
    randomstick=random.randint(0,10)
    pic=stickers[randomstick]
    bot.sendMessage(chat_id=update.message.chat_id, text="Создатель просил передать...", reply_markup=markup)
    bot.sendSticker(chat_id=update.message.chat_id, sticker=pic, reply_markup=markup);
proof_handler = CommandHandler('proof', proof)
dispatcher.add_handler(proof_handler)

def grustno(bot, update):
    pic=open('s1200.jpeg', 'rb')
    bot.send_photo(chat_id=update.message.chat_id, photo=pic);
    bot.sendMessage(chat_id=update.message.chat_id, text="Ни грустииии", reply_markup=markup)
grustno_handler = CommandHandler('grustno', grustno)
dispatcher.add_handler(grustno_handler)
#ставим вебхук
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=config.token)
updater.bot.set_webhook("https://stresscatbot.herokuapp.com/" + config.token)

