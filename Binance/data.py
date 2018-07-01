# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 23:07:35 2018

@author: jonas
"""

from binance.client import Client
from collections import defaultdict
from time import time

key = ""
secret = ""

from forex_python.converter import CurrencyRates
def binaUpdate():
    usd_eur = CurrencyRates().get_rates('USD')['EUR']
    
    client = Client(key, secret)
    
    coins = defaultdict(float)
    for a in client.get_account()['balances']:
        amount = float(a['free'])
        if amount!=.0:
            coins[a['asset']]+=amount
    
    combinedValue = .0        
    btc_value = float(client.get_symbol_ticker(symbol='BTCUSDT')['price'])*usd_eur
    data = {}
    for a in coins:
        amount = coins[a]
        if a!='BTC':
            price = float(client.get_symbol_ticker(symbol=a+'BTC')['price'])*btc_value
        else:
            price = btc_value
        value = price * amount
        data[a] = {'amount' : amount, 'price' : price, 'value' : value}
        combinedValue += value
    
    return {'marketname':'Binance', 'timestamp':time(),'value':combinedValue,'coinData':data}

if __name__ == "__main__":
    print(binaUpdate())
