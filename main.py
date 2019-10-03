import telebot
import logging
import random

bot = telebot.TeleBot('942993404:AAGP1GoLF6AC94O5MsAXD3qRSYsPAp4MmkI')
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


@bot.message_handler(commands=['suck'])
def suck_message(message):
    suck = ['Орловского', 'Воэнкома', 'себя']
    suck = random.choice(suck)
    bot.send_message(message.chat.id,  'Cоси извращенец у %s' % suck)



@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
        print('Привет')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    else:
        str = "Сам " + message.text
        bot.send_message(message.chat.id, str)


bot.polling()
