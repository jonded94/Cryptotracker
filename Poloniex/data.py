# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 23:07:35 2018

@author: jonas
"""

import poloniex
from collections import defaultdict
from time import time

apikey = ""
secret = ""

from forex_python.converter import CurrencyRates
def poloUpdate():
    usd_eur = CurrencyRates().get_rates('USD')['EUR']
    
    client = poloniex.Poloniex(apikey=apikey,secret=secret)
    
    coins = defaultdict(float)
    for name, amount in client.returnBalances().items():
        if amount!=.0:
            coins[name]+=amount
    
    combinedValue = .0        
    prices = client.returnTicker()
    btc_value = prices['USDT_BTC']['last']*usd_eur
    data = {}
    for a in coins:
        amount = coins[a]
        if a!='BTC':
            price = prices['BTC_'+a]['last']*btc_value
        else:
            price = btc_value
        value = price * amount
        data[a] = {'amount' : amount, 'price' : price, 'value' : value}
        combinedValue += value
    
    return {'marketname':'Poloniex', 'timestamp':time(),'value':combinedValue,'coinData':data}

if __name__ == "__main__":
    print(poloUpdate())
