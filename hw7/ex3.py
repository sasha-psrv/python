# Задача 3. Добавьте в telegram-бота игру «Угадай числа». Бот
# загадывает число от 1 до 1000. Когда игрок угадывает его, бот
# выводит количество сделанных ходов.

import telebot
from random import randint

bot = telebot.TeleBot('TOKEN')

min_number = 1
max_number = 1000

number = randint(min_number, max_number)

attempts = 0

@bot.message_handler(commands=['start'])
def start_message(message):
    global attempts 
    attempts = 0 
    bot.send_message(message.chat.id, 'Привет! Я загадал число от {} до {}. Попробуй угадать!'.format(min_number, max_number))

@bot.message_handler(content_types=['text'])
def check_number(message):
    global attempts  
    try:
        guess = int(message.text)
        if guess < min_number or guess > max_number:
            bot.send_message(message.chat.id, 'Число должно быть от {} до {}.'.format(min_number, max_number))
        elif guess < number:
            attempts += 1 
            bot.send_message(message.chat.id, 'Загаданное число больше.'.format(attempts))
        elif guess > number:
            attempts += 1 
            bot.send_message(message.chat.id, 'Загаданное число меньше.'.format(attempts))
        else:
            bot.send_message(message.chat.id, 'Поздравляю, ты угадал! Количество сделанных ходов - {}'.format(attempts))
            bot.stop_polling() 
    except ValueError:
        bot.send_message(message.chat.id, 'Это не число.')

bot.polling()