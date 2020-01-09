headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

from flask import Flask, render_template
from urllib.request import urlopen, Request
import json
from datetime import datetime

def getDate(): #returns date as a string in the format mm-dd-yyyy
    date = datetime.now().date() #gets the date
    date = date.strftime("%m-%d-%Y") #converts to string
    return date

def checkDate(): #compares the difference in dates
    t1 = datetime.now().date().strftime("%m-%d-%Y") #converts to string
    t2 = datetime.now().date().strftime("%m-%d-%Y")
    t3 = int(t1.split("-")[0])
    t4 = int(t2.split("-")[0])
    print(t3)

def checkDate2(date): #compares the difference in dates
    prevDate = date.split("-")
    nowDate = getDate().split("-")
    if int(nowDate[0]) - int(prevDate[0]) == 0 and int(nowDate[1]) - int(prevDate[1]) == 0:
        return 0
    if int(nowDate[0]) - int(prevDate[0]) == 0 and int(nowDate[1]) - int(prevDate[1]) == 1:
        return 1
    else:
        return 2 

def getCard():
    request = Request('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1',headers = headers)
    response = urlopen(request).read()
    data = json.loads(response)
    deck_id = data['deck_id']
    request = Request('https://deckofcardsapi.com/api/deck/{}/draw/?count=2'.format(deck_id),headers = headers)
    response = urlopen(request).read()
    data = json.loads(response)
    return(data['cards'][0]['code'])
