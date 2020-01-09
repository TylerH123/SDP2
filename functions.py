from flask import Flask, render_template
from urllib.request import urlopen, Request
import json
from datetime import datetime

deck = []

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

def getDate(): #returns date as a string in the format mm-dd-yyyy
    date = datetime.now().date() #gets the date
    date = date.strftime("%m-%d-%Y") #converts to string
    return date

def checkDate(date): #compares the difference in dates
    prevDate = date.split("-")
    nowDate = getDate().split("-")
    if int(nowDate[0]) - int(prevDate[0]) == 0 and int(nowDate[1]) - int(prevDate[1]) == 1:
        return 1
    elif int(nowDate[1]) - int(prevDate[1]) > 0 or int(nowDate[0]) - int(prevDate[0]) > 1:
        return 2

def checkDiceWin(dict):
    if dict['roll1'] > dict['roll2']:
        return True
    else:
        return False

def getNewDeck():
    request = Request('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1',headers = headers)
    response = urlopen(request).read()
    data = json.loads(response)
    deckID = data['deck_id']
    request = Request('https://deckofcardsapi.com/api/deck/{}/draw/?count=52'.format(deckID),headers = headers)
    response = urlopen(request).read()
    data = json.loads(response)
    deck.extend(data['cards'])

def getCard():
    if len(deck) == 0:
        getNewDeck()
    out = deck[0]
    deck.pop(0)
    return(out)

print(getCard())
