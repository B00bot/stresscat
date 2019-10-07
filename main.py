# -*- coding: utf-8 -*-
import requests
import config
import telebot
from telebot import types
from telegram.ext import Updater
import os

TOKEN = "862281743:AAEvvJc2tldFHZWXqC540GKAxvSPxpyvqPc"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)

bot = telebot.TeleBot(config.token)

bot.process_new_updates([update])

@bot.message_handler(content_types=["text"])
def get_text_messages(message):
	if message.text == "Привет":
		bot.send_message(message.from_user.id, "Привет, если хочешь узнать тайну, отправь /secret. Если нужны доказательства - отправь /proof")
	elif message.text == "/help":
		bot.send_message(message.from_user.id, "Напиши привет")
	elif message.text == "/secret":
		bot.send_message(message.from_user.id, "Мой создатель любит Лапу")
	elif message.text == "/proof":
		bot.send_photo(message.from_user.id, open('tsmock.jpg', 'rb'));
	else:
		bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")	

updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
bot.remove_webhook()
updater.bot.set_webhook("https://www.stresscatbot.herokuapp.com/" + TOKEN)
updater.idle()
