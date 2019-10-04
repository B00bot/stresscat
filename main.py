import telebot
from telebot import types
import requests  
import datetime
import requests

url = "https://api.telegram.org/bot<845739116:AAHTjdzhhe526OLCj1uycnJG6jg2H3NXxfk>/"
class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

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
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           send_mess(get_chat_id(last_update(get_updates_json(url))), 'test')
           update_id += 1
    sleep(1)       

if __name__ == '__main__':  
    main()		
