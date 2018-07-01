# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 17:49:35 2018

@author: jonas
"""
import sys
sys.path.insert(0, "/home/pi/crypto")
import json
import datetime as dt
from simpletable import SimpleTable, HTMLPage

with open('/home/pi/crypto/data.json', 'r') as f:
     data = json.load(f)

page = HTMLPage()

coinNames = {
'BTC' : 'Bitcoin',
'BTG' : 'Bitcoin Gold',
'ETH' : 'Ethereum',
'IOT' : 'IOTA',
'XRP' : 'Ripple',
'NEO' : 'NEO',
'XLM' : 'Stellar',
'ADA' : 'Cardano',
'EOS' : 'EOS',
'STR' : 'Stellar',
'BCH' : 'Bitcoin Cash',
'XEM' : 'NEM',
'NANO' : 'NANO',
'BNB' : 'Binance Coin'
}


totalValue = 0.0
data = data[-1]
for i in data:
    name = i['marketname']
    res = []
    for j, k in i['coinData'].items():
        if k['value']>.5:
            res.append([coinNames[j.upper()] + ' (' + j.upper() + ')', round(k['amount'],4), str(round(k['price'],3))+' €', str(round(k['value'],2))+' €'])
    res.sort(key=lambda x:x[0])
    res.append([dt.datetime.fromtimestamp(round(i['timestamp'],0)),'','',str(round(i['value'],2))+' €'])
    totalValue += i['value']
    page.add_table(SimpleTable( [['Coinname', 'Amount', 'Market Price', 'Value']] + res,
        header_row=[name],
        css_class='mytable',header_colspan=4))
page.add_table(SimpleTable([['Combined Value: ', '<b>' + str(round(totalValue,2)) + ' €</b>']],
        css_class='mytable2'))
css = """
table.mytable {
    font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
    border-collapse: collapse;
    width=100%;
	margin=0;
    border: 1px solid #ddd;
}
table.mytable th, td {
    padding: 9px;
    text-align: center;
    border-bottom: 1px solid #ddd;
}
table.mytable th, tr:nth-child(2) td{
    color: white;
	font-weight: bold;
}
table.mytable th {
    background-color: #4CAF50;
	font-size: larger;
}
table.mytable tr:nth-child(2) td{
    background-color: #6EC162;
}
table.mytable tr:last-child td:first-child {
    font-weight: normal;
}
table.mytable tr:last-child {
    border-top: 3px solid #ddd;
}
table.mytable td:first-child, td:nth-child(4) {
    font-weight: bold;
}
table.mytable td:first-child, td:nth-child(3) {
    border-right:1px solid #ccc;
}
table.mytable tr:nth-child(even) {
    background-color: #f2f2f2;
}
table.mytable tr:hover {
    background-color: #e0e0e0;
}
#code {
    display:inline;
    font-family: courier;
    color: #3d9400;
}
#string {
    display:inline;
    font-weight: bold;
}
table.mytable2 {
    font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
    border-collapse: collapse;
    width=100%;
    border: 1px solid #ddd;
	background-color: #6EC162;
    color: white;
    padding: 15px;
    text-align: center;
}
"""
page.css = css
page.save('/home/pi/crypto/test.html')
