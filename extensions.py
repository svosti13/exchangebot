import json
import requests
from config import keys

class ExchangeException(Exception):
    pass

class Exchange:
    @staticmethod
    def get_price(quote:str,base:str,amount:str):
        if quote == base:
            raise ExchangeException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ExchangeException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ExchangeException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ExchangeException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={quote_ticker}&symbols={base_ticker}')
        total_base=json.loads(r.content)["rates"][keys[base]]
        total_base = total_base * amount
        return total_base
