# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 23:07:35 2018

@author: jonas
"""

import btcde
import logging
from collections import defaultdict
from time import time, sleep

key = ""
secret = ""

def bitcUpdate():
    conn = btcde.Connection(key, secret)
    
    logging.getLogger().setLevel(logging.ERROR)
    logging.getLogger('requests.packages.urllib3').setLevel(logging.ERROR)
    
    coins = defaultdict(float)
    for name, data in conn.showAccountInfo()['data']['balances'].items():
        amount = float(data['total_amount'])
        if amount!=.0:
            coins[name]+=amount
    del coins["btg"]        
    combinedValue = .0
    data = {}
    for a in coins:
        sleep(.5)
        amount = coins[a]
        price = float(conn.showRates(a+'eur')['rates']['rate_weighted'])
        value = price * amount
        data[a] = {'amount' : amount, 'price' : price, 'value' : value}
        combinedValue += value
    
    return {'marketname':'bitcoin.de', 'timestamp':time(),'value':combinedValue,'coinData':data}

if __name__ == "__main__":
    print(bitcUpdate())
