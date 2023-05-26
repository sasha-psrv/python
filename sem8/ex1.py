# Задача 1. Напишите чат-бота, который записывает
# сообщения всех пользователей, которые ему
# написали


import telebot
import requests
from telebot import types

bot = telebot.TeleBot("TOKEN")

markup = types.ReplyKeyboardMarkup(row_width=1)
btn_reg = types.KeyboardButton('регистрация')
btn_alarm = types.KeyboardButton('оповещение')
markup.add(btn_reg, btn_alarm)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.from_user.id, "Приветик, я бот Саши",reply_markup= markup)
	
@bot.message_handler(content_types=['text'])
def text_messege(message):
	# print(message)
	data = open('log.txt', mode='a', encoding='utf-8')
	text = f'{message.from_user.first_name} {message.from_user.last_name}: {message.text}\n'
	data.write(text)
	data.close()
	if message.text == 'регистрация':
		data = open('registed_user.txt', mode='r', encoding='utf-8')
		id_list = data.readlines()
		data.close()
		id_list = list(id[:-1] for id in id_list)
		if str(message.from_user.id) not in id_list:
			data = open('registed_user.txt', mode='a', encoding='utf-8')
			data.write(f'{message.from_user.id}\n')
			data.close()
			bot.reply_to(message, 'регистрация прошла успешно)')
		else:
			bot.reply_to(message, 'вы уже зарегистрированы)')
	elif message.text == 'оповещение':
		data = open('registed_user.txt', mode='r', encoding='utf-8')
		id_list = data.read().split('\n')
		data.close()
		id_list = id_list[:-1]
		for id in id_list:
			if id != '':
				bot.send_message(id, 'совещание через 5 минут')
	

bot.polling()