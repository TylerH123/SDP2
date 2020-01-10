from flask import Flask, render_template
from urllib.request import urlopen, Request
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

deck = []
playerDeck = []
dealerDeck = []
turn = "player"

def getNewDeck():
    request = Request('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1',headers = headers)
    response = urlopen(request).read()
    data = json.loads(response)
    deckID = data['deck_id']
    request = Request('https://deckofcardsapi.com/api/deck/{}/draw/?count=52'.format(deckID),headers = headers)
    response = urlopen(request).read()
    data = json.loads(response)
    deck.extend(data['cards'])

def addCard(d):
    if len(deck) == 0:
        getNewDeck()
    d.append((deck[0]['value'],deck[0]['image']))
    deck.pop(0)

def start():
    playerDeck.append((deck[0]['value'],deck[0]['image']))
    deck.pop(0)
    playerDeck.append((deck[0]['value'],deck[0]['image']))
    deck.pop(0)
    dealerDeck.append((deck[0]['value'],deck[0]['image'],"unflipped"))
    deck.pop(0)
    dealerDeck.append((deck[0]['value'],deck[0]['image'],"flipped"))
    deck.pop(0)

def clearDeck(d):
    if d == "all":
        deck.clear()
        playerDeck.clear()
        dealerDeck.clear()
    elif d == "player":
        playerDeck.clear()
    elif d == "dealer":
        dealerDeck.clear()

def checkTotal(deck):
    val = 0
    for c in deck:
        if c[0] == "JACK" or c[0] == "QUEEN" or c[0] == "KING":
            val += 10
        elif c[0] == "ACE":
            val += 11
        else:
            val += int(c[0])
    return val

def dealerTurn():
    dealerDeck.pop(0)
    deal    erDeck.insert(0, (deck[0]['value'],deck[0]['image'],"flipped"))
    while checkTotal(dealerDeck) < 17:
        addCard(dealerDeck)
