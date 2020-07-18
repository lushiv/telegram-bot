import requests
from config import BotConfig
import json 

# Cryptp API
def get_cms_data(crypto):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    params = {'symbol': crypto, 'convert': 'USD'}
    headers = {'X-CMC_PRO_API_KEY': BotConfig.cmc_token}

    r = requests.get(url, headers=headers, params=params).json()
    price = r['data'][crypto]['quote']['USD']['price']
    print(price)
    return price