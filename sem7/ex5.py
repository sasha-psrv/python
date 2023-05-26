# Задача 5. Создайте telegram-бота, добавьте в него
# метод приветствия пользователя.

import telebot
import requests

bot = telebot.TeleBot("TOKEN")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Приветик, как твои дела?")


@bot.message_handler(content_types=['text'])
def greetings(message):
	text = message.text
	if 'Погода' in text:
		req = requests.get('https://wttr.in/?0T')
        bot.reply_to(message, req.text)
	elif 'Привет' in text:
		bot.reply_to(message, f"Привет, {message.from_user.first_name}")
    elif text == 'Погода':
		req = requests.get('https://wttr.in/?0T')
        bot.reply_to(message, req.text)


	 
	
bot.polling()