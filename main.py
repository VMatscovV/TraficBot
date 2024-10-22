import time

import telebot
from telebot import types

import selparser
import exel


bot = telebot.TeleBot('7701163526:AAEEmBXsGbpwXOsSJi275gxA7KCoHGQ4Qls')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Send request")
    btn2 = types.KeyboardButton("Help")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я тестовый бот".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Send request"):
        bot.send_message(message.chat.id, text="Запустил сбор данных, просьба не беспокоить 10 минут")
        result = selparser.main_pars()
        exel.main(result)
        bot.send_document(message.chat.id, open(r'Ymarket.xlsx', 'rb'))



    elif (message.text == "Help"):
        bot.send_message(message.chat.id, "Пока пусто...")

    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


while True:
    try:
        bot.polling(none_stop=True)
    except:
        time.sleep(5)