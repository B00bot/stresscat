# -*- coding: utf-8 -*-
import requests
import config
import telebot
from telebot import types
from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters
import os
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(config.token)
dispatcher = updater.dispatcher
bot = telebot.TeleBot(config.token)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

hi_handler = CommandHandler('привет', hi)
dispatcher.add_handler(hi_handler)
def hi():
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, если хочешь узнать тайну, отправь /secret. Если нужны доказательства - отправь /proof")
	
secret_handler = CommandHandler('/secret', secret)
dispatcher.add_handler(secret_handler)
def secret():
    if message.text == "secret":
        bot.send_message(message.from_user.id, "Мой создатель любит Лапу")

proof_handler = CommandHandler('/proof', proof)
def proof()
    if message.text == "Привет":
        bot.send_photo(message.from_user.id, open('tsmock.jpg', 'rb'));
dispatcher.add_handler(proof_handler)

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=config.token)
updater.bot.set_webhook("https://stresscatbot.herokuapp.com/" + config.token)
updater.idle()
