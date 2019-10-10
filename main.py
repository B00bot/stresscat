# -*- coding: utf-8 -*-
import requests
import config
import telebot
from telebot import types
from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters
import os
import logging
import random
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(config.token)
dispatcher = updater.dispatcher
bot = telebot.TeleBot(config.token)
def start(bot, update):
        bot.sendMessage(chat_id=update.message.chat_id, text="Привет, если хочешь узнать тайну, отправь /secret Если нужны доказательства - отправь /proof Если грустно - отправь /grustno")	
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def secret(bot, update):
        bot.sendMessage(chat_id=update.message.chat_id, text="Мой создатель любит Лапу")
secret_handler = CommandHandler('secret', secret)
dispatcher.add_handler(secret_handler)

def help(bot, update):
        bot.sendMessage(chat_id=update.message.chat_id, text="Если хочешь узнать тайну, отправь /secret Если нужны доказательства - отправь /proof Если грустно - отправь /grustno")	
help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

#stickers for random
stick1="CAADAgADCwADlp-MDpuVH3sws_a7FgQ"
stick2="CAADAgAD7g0AAqgILwj_8DhBu2dnDRYE"
stick3="CAADBAADfQADzjkIDSgZQLclD7jiFgQ"
stick4="CAADBAADRAADzjkIDbv4-ULKD6hiFgQ"
stick5="CAADAgAD0gIAArnzlwt4AXAE0tVijhYE"

def proof(bot, update):
    randomstick=random.randint(1,5)
    if randomstick==1:
        pic=stick1
    elif randomstick==2:
        pic=stick2
    elif randomstick==3:
        pic=stick3
    elif randomstick==4:
        pic=stick4
    elif randomstick==5:
        pic=stick5
    bot.sendSticker(chat_id=update.message.chat_id, sticker=pic);
proof_handler = CommandHandler('proof', proof)
dispatcher.add_handler(proof_handler)

def grustno(bot, update):
    pic=open('s1200.jpeg', 'rb')
    bot.send_photo(chat_id=update.message.chat_id, photo=pic);
    bot.sendMessage(chat_id=update.message.chat_id, text="Ни грустииии")
grustno_handler = CommandHandler('grustno', grustno)
dispatcher.add_handler(grustno_handler)


btns = ReplyKeyboardMarkup(resize_keyboard=True).add(button_secret("Секрет", data=secret), button_proof("Доказательство", data=proof), button_sad("Мне грустно", data=grustno), button_help("Нипанятнаа", data=help)) 



updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=config.token)
updater.bot.set_webhook("https://stresscatbot.herokuapp.com/" + config.token)
updater.idle()
