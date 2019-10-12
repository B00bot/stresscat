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



def startpg(bot, update):
    startmenu=types.ReplyKeyboardMarkup(True, False)
    startmenu.row('Секрет', 'Доказательство')
    startmenu.row('Грустно')
    startmenu.row('Нипанятнаа')
    bot.send_message(update.message.chat.id, 'Привет. Если хочешь узнать секрет, нажми секрет. Если нужно доказательство, нажми Доказательство. Если грустно, нажми Грустно. Если нужна помошь - нажми Нипанятнаа', reply_markup=startmenu)

def secret(bot, update):
    incoming=update.message.text
    if incoming=='Секрет':
        bot.sendMessage(chat_id=update.message.chat_id, text="Мой создатель любит Лапу")
secret_handler = MessageHandler(Filters.text, secret)
dispatcher.add_handler(secret_handler)

def help(bot, update):
    incoming=update.message.text
    if incoming=='Нипанятнаа':
        bot.sendMessage(chat_id=update.message.chat_id, text="Если хочешь узнать тайну, отправь /secret Если нужны доказательства - отправь /proof Если грустно - отправь /grustno")	
help_handler = MessageHandler(Filters.text, help)
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
    incoming=update.message.text
    if incoming=='Доказательство':
        bot.sendSticker(chat_id=update.message.chat_id, sticker=pic)
proof_handler = MessageHandler(Filters.text, proof)
dispatcher.add_handler(proof_handler)

def grustno(bot, update):
    incoming=update.message.text
    if incoming=='Грустно':
        pic=open('s1200.jpeg', 'rb')
        bot.send_photo(chat_id=update.message.chat_id, photo=pic);
        bot.sendMessage(chat_id=update.message.chat_id, text="Ни грустииии")
grustno_handler = MessageHandler(Filters.text, grustno)
dispatcher.add_handler(grustno_handler)

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=config.token)
updater.bot.set_webhook("https://stresscatbot.herokuapp.com/" + config.token)
updater.idle()
