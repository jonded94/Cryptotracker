# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 13:50:01 2018

@author: jonas
"""

import json

with open('/home/pi/crypto/data.json', 'r') as f:
     data = json.load(f)

res = []
for i in data:
    values = {}
    for j in i:
        values[j['marketname']] = j['value']
        timestamp=j['timestamp']
    res.append([timestamp,values])
    
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime as dt

markets = ['Bitfinex', 'Binance', 'Poloniex', 'bitcoin.de']

X  = np.array([dt.datetime.fromtimestamp(x[0]) for x in res])
Y_old = np.array([[x[1][i] for x in res] for i in markets])
Y = np.copy(Y_old)

fig = plt.figure()
ax = fig.add_subplot(111)

for i in range(len(Y)):
    if i!=0:
        Y[i]+=Y[i-1]
		
step=int(len(X)*3/5)
start=int(len(X)*1/5)
for i in range(len(Y)):
	plt.plot_date(x=X,y=Y[i],label=markets[i], fmt='-')
	for a,b,c in zip(X[start::step], Y[i][start::step], Y_old[i][start::step]):
		plt.text(a, b, str(round(c,2)),horizontalalignment='center',verticalalignment='center',bbox=dict(boxstyle="round4",facecolor='white', alpha=0.8), color="black")
	if i==0:
		plt.fill_between(X, 0,Y[0],alpha=.2)
	else:
		plt.fill_between(X, Y[i-1],Y[i],alpha=.2)

for a,b in zip(X[start::step], Y[-1][start::step]):
	plt.text(a, b*1.1, str(round(b,2)),horizontalalignment='center',verticalalignment='center',bbox=dict(boxstyle="round4",facecolor='black', alpha=0.8), color="white")
plt.xlim((X[0],X[-1]))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m %H:%M'))
plt.gcf().autofmt_xdate()
plt.ylim((0,max(Y[-1])))

# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.85, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1.02, 0.5))

# Put a legend to the right of the current axis
plt.grid()
plt.show()
plt.savefig('/home/pi/crypto/test.pdf')
plt.savefig('/home/pi/crypto/test.png')
