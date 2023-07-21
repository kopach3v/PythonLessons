import telebot
import requests
from pybit.unified_trading import HTTP

import bybit_api
from Keys import telegram_token, secret_key,api_key
from bybit_api import get_tickers




bot = telebot.TeleBot(telegram_token)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,'Привет, введите название монеты в формате: BTCUSDT')

@bot.message_handler()
def coin_price(message):

    try:
        coin_name_input = message.text.upper()
        bot.reply_to(message,f'Price: {bybit_api.get_tickers.result_symbol} {get_tickers.result_price}$')
    except:
        bot.reply_to(message,"Я не знаю такую монету")



bot.infinity_polling()