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
def start(update, context):
    if context == "/start":
        bot.send_message(message.from_user.id, "Напиши привет")
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def hi(update, context):
    if context == "Привет":
        bot.send_message(message.from_user.id, "Привет, если хочешь узнать тайну, отправь /secret. Если нужны доказательства - отправь /proof")	
hi_handler = CommandHandler('привет', hi)
dispatcher.add_handler(hi_handler)

def secret(update, context):
    if context == "/secret":
        bot.send_message(message.from_user.id, "Мой создатель любит Лапу")
secret_handler = CommandHandler('/secret', secret)
dispatcher.add_handler(secret_handler)

def proof(update, context):
    if context == "/proof":
        bot.send_photo(message.from_user.id, open('tsmock.jpg', 'rb'));
proof_handler = CommandHandler('/proof', proof)
dispatcher.add_handler(proof_handler)

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=config.token)
updater.bot.set_webhook("https://stresscatbot.herokuapp.com/" + config.token)
updater.idle()
