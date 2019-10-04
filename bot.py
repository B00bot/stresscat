# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types
import re

from telegram.ext import Updater, MessageHandler, Filters

bot = telebot.TeleBot(config.token)

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
def main():
    updater = Updater(config.token)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
