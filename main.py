# -*- coding: utf-8 -*-
import requests
import config
import telebot
from telebot import types
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
import os
import logging
import random
updater=Updater(config.token)
TOKEN=config.token
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
PORT = int(os.environ.get('PORT', '8443'))
bot = telebot.TeleBot(config.token)

startmenu=types.ReplyKeyboardMarkup(True, False)
startmenu.row('Секрет', 'Доказательство')
startmenu.row('Грустно')
startmenu.row('Нипанятнаа')
updater.dispatcher.add_handler(message_handler(bot, update)

#stickers for random
stick1="CAADAgADCwADlp-MDpuVH3sws_a7FgQ"
stick2="CAADAgAD7g0AAqgILwj_8DhBu2dnDRYE"
stick3="CAADBAADfQADzjkIDSgZQLclD7jiFgQ"
stick4="CAADBAADRAADzjkIDbv4-ULKD6hiFgQ"
stick5="CAADAgAD0gIAArnzlwt4AXAE0tVijhYE"

@bot.message_handler(content_types=["text"])
def secret(message):
    incoming=message.text
    if incoming=='/start':
        bot.send_message(message.chat.id, 'Привет. Если хочешь узнать секрет, нажми секрет. Если нужно доказательство, нажми Доказательство. Если грустно, нажми Грустно. Если нужна помошь - нажми Нипанятнаа', reply_markup=startmenu)

@bot.message_handler(content_types=["text"])
def secret(message):
    incoming=message.text
    if incoming=='Секрет':
        bot.sendMessage(chat_id=message.chat_id, text="Мой создатель любит Лапу")

@bot.message_handler(content_types=["text"])
def help(message):
    incoming=message.text
    if incoming=='Нипанятнаа':
        bot.sendMessage(chat_id=message.chat_id, text="Если хочешь узнать тайну, отправь /secret Если нужны доказательства - отправь /proof Если грустно - отправь /grustno")	

@bot.message_handler(content_types=["text"])
def proof(message):
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
    incoming=message.text
    if incoming=='Доказательство':
        bot.sendSticker(chat_id=message.chat_id, sticker=pic)

@bot.message_handler(content_types=["text"])
def grustno(message):
    incoming=message.text
    if incoming=='Грустно':
        pic=open('s1200.jpeg', 'rb')
        bot.send_photo(chat_id=message.chat_id, photo=pic)
        bot.sendMessage(chat_id=message.chat_id, text="Ни грустииии")

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://stresscatbot.herokuapp.com/" + TOKEN)
updater.idle()
