# Задача 2. Напишите программу, которая позволяет считывать из файла вопрос, отвечать на него и отправлять ответ обратно пользователю.


import telebot

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Какой у вас вопрос или проблема?')


@bot.message_handler(content_types=['text'])
def handle_message(message):
    data = open('answer.txt', mode='a', encoding='utf-8')
    text = f'{message.from_user.id}: {message.text}\n'
    data.write(text)
    data.close()


quetion = '752176311:почему ветер дует'.split(':') 
input = 'потому что деревья качаются'
bot.send_message(quetion[0], f'вы спрашивали: {quetion[1]}')
bot.send_message(quetion[0], f'мы отвечаем: {input}')

bot.polling()

