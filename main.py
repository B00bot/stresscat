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
def start(bot, update):
        bot.sendMessage(chat_id=update.message.chat_id, text="Привет, если хочешь узнать тайну, отправь /secret. Если нужны доказательства - отправь /proof")	
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def secret(bot, update):
        bot.sendMessage(chat_id=update.message.chat_id, text="Мой создатель любит Лапу")
secret_handler = CommandHandler('secret', secret)
dispatcher.add_handler(secret_handler)

def proof(bot, update):
    pic=open('tsmock.jpg', 'rb')
    bot.send_photo(chat_id=update.message.chat_id, photo=pic);
proof_handler = CommandHandler('proof', proof)
dispatcher.add_handler(proof_handler)

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=config.token)
updater.bot.set_webhook("https://stresscatbot.herokuapp.com/" + config.token)
updater.idle()
