# -*- coding: utf-8 -*-
import telebot
from telebot import types
from config import token

bot = telebot.TeleBot(token)

class Keyboard:
    def keyboard(message):
        markup = types.ReplyKeyboardMarkup()
        button1 = types.KeyboardButton('/secret')
        button2 = types.KeyboardButton('/proof')
        button3 = types.KeyboardButton('/grustno')
        button4 = types.KeyboardButton('/help')
        markup.row(button1, button2, button3)
        markup.row(button4)
        bot.send_message(message.chat.id, 'Main menu: ', reply_markup=markup)
