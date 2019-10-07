# -*- coding: utf-8 -*-
import requests
import config
import telebot
from telebot import types
import os

TOKEN = "TOKEN"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)
# add handlers
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://<appname>.herokuapp.com/" + TOKEN)
updater.idle()

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
		
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)

        except Exception as e:
            print(e) 
            time.sleep(15)
