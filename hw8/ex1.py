# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

import datetime
import telebot

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Какой у вас вопрос или проблема?')



@bot.message_handler(content_types=['text'])
def handle_message(message):
    data = open('support.txt', mode='a', encoding='utf-8')
    text = f'{message.from_user.first_name}{message.from_user.id}: {message.text}\n'
    data.write(text)
    data.close()
    bot.send_message(message.chat.id, 'Ваше обращение принято.')


bot.polling()