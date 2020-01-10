from flask import Flask, render_template
from urllib.request import urlopen, Request
import json
import db as dbase

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
gameStatus = "ingame"

def getNewDeck():
    request = Request('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=2',headers = headers)
    response = urlopen(request).read()
    data = json.loads(response)
    deckID = data['deck_id']
    request = Request('https://deckofcardsapi.com/api/deck/{}/draw/?count=104'.format(deckID),headers = headers)
    response = urlopen(request).read()
    data = json.loads(response)
    deck.extend(data['cards'])

def addCard(d,f):
    if len(deck) == 0:
        getNewDeck()
    if (d == playerDeck):
        d.append((deck[0]['value'],deck[0]['image'],f))
    else:
        d.append((deck[0]['value'],deck[0]['image'],f))
    deck.pop(0)

def start():
    global gameStatus, turn
    gameStatus = "ingame"
    turn = "player"
    #print(gameStatus + " s")
    #print(turn + " s")
    clearDeck(playerDeck)
    clearDeck(dealerDeck)
    while len(playerDeck) < 2:
        addCard(playerDeck,"flipped")
    if len(dealerDeck) < 2:
        addCard(dealerDeck,"unflipped")
        addCard(dealerDeck,"flipped")

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
    tup = (dealerDeck[0][0],dealerDeck[0][1],"flipped")
    dealerDeck.pop(0)
    dealerDeck.insert(0, tup)
    while checkTotal(dealerDeck) < 17:
        addCard(dealerDeck,"flipped")

def play():
    global gameStatus
    #print(gameStatus)
    #print(playerDeck)
    #print(turn)
    if gameStatus == "ingame":
        #print(playerDeck)
        if checkTotal(playerDeck) < 21:
            if turn == "player":
                addCard(playerDeck,"flipped")
            if turn == "dealer":
                dealerTurn()
        if checkTotal(playerDeck) > 21:
            #print(checkTotal(playerDeck))
            gameStatus = "lost"
            dbase.userInfo['coins'] -= 100
            gameStatus = "standby"
        if turn == "dealer":
            if checkTotal(playerDeck) == checkTotal(dealerDeck):
                gameStatus = "tie"
            if checkTotal(playerDeck) > checkTotal(dealerDeck):
                gameStatus = "win"
                dbase.userInfo['coins'] += 150
                gameStatus = "standby"

def checkBJ():
    if (playerDeck[0][0] == "ACE" or playerDeck[1][0] == "ACE") and checkTotal(playerDeck) == 21:
        gameStatus = "win"
        dbase.userInfo['coins'] += 150
        gameStatus = "standby"
