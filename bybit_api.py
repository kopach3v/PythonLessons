from pybit.unified_trading import HTTP
from Keys import telegram_token, secret_key,api_key
from bot import coin_price

def get_tickers():
    session = HTTP(api_key=api_key, api_secret=secret_key, testnet=False)

    result = session.get_tickers(
        category="spot", symbol=coin_price.coin_name_input).get('result')['list'][0]
    result_symbol = result['symbol']
    result_price = result['lastPrice']

