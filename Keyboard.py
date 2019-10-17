# -*- coding: utf-8 -*-
import telebot
from telebot import types
from config import token

bot = telebot.TeleBot(token)

class Keyboard:
    def start_keyboard(message):
        markup = types.ReplyKeyboardMarkup()
        button1 = types.KeyboardButton('\ud83d\udcbc Simple Keyboard')# Для того что бы к кнопке или сообщению добавить Emoji нужно
        button2 = types.KeyboardButton('\ud83c\udfe2 Inline Keyboard')#в базе юникода выбрать смайл, взять его индекс, и забить
        button3 = types.KeyboardButton('\ud83d\udcf2 Callback Inline')#этот индекс на сайт https://www.charbase.com и оттуда взять код из графы JavaEscape. Я делал так.
        markup.row(button1, button2)#2 кнопки в ряд
        markup.row(button3)#одна кнопка в ряд. Думаю принцип понятен
        bot.send_message(message.chat.id, 'Main menu: ', reply_markup=markup)#Важный момент, если переменная markup которую вы создали и заполнили выше носит другое название, например krakozyabra, то тут нужно будет указать krakozyabra
