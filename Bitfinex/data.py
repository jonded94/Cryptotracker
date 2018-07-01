# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 23:07:35 2018

@author: jonas
"""

import bitfinex
from collections import defaultdict
from time import time

key = ""
secret = ""

from forex_python.converter import CurrencyRates
def bitfUpdate():
    usd_eur = CurrencyRates().get_rates('USD')['EUR']
    
    client = bitfinex.TradeClient(key, secret)
    pclient = bitfinex.Client()
    
    coins = defaultdict(float)
    for a in client.balances():
        amount = float(a['amount'])
        if amount!=.0:
            coins[a['currency'].upper()]+=amount
    
    combinedValue = .0
    data = {}
    for a in coins:
        amount = coins[a]
        price = pclient.ticker(a+'usd')['mid']*usd_eur
        value = price * amount
        data[a] = {'amount' : amount, 'price' : price, 'value' : value}
        combinedValue += value
    
    return {'marketname':'Bitfinex','timestamp':time(),'value':combinedValue,'coinData':data}

if __name__ == "__main__":
    print(bitfUpdate())
