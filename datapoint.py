# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 13:37:21 2018

@author: jonas
"""

from Bitfinex.data import bitfUpdate
from Binance.data import binaUpdate
from Poloniex.data import poloUpdate
from bitcoin_de.data import bitcUpdate

import json
import datetime

with open('/home/pi/crypto/data.json', 'r') as f:
     data = json.load(f)

res = []
print("Getting Bitfinex...")
start = datetime.datetime.now()
res.append(bitfUpdate())
end = datetime.datetime.now()
elapsed = end - start
print("Took",elapsed) 


print("Getting Binance...")
start = datetime.datetime.now()
res.append(binaUpdate())
end = datetime.datetime.now()
elapsed = end - start
print("Took",elapsed) 


print("Getting Poloniex...")
start = datetime.datetime.now()
res.append(poloUpdate())
end = datetime.datetime.now()
elapsed = end - start
print("Took",elapsed) 


print("Getting bitcoin.de...")
start = datetime.datetime.now()
res.append(bitcUpdate())
end = datetime.datetime.now()
elapsed = end - start
print("Took",elapsed) 

data.append(res)

with open('/home/pi/crypto/data.json', 'w') as f:
     json.dump(data, f)
