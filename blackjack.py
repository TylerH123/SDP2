from flask import Flask, flash
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
wager = 0

def getNewDeck(): #gets a new set of 312 cards. the values and images are stored into deck array
    request = Request('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6',headers = headers)
    response = urlopen(request).read()
    data = json.loads(response)
    deckID = data['deck_id']
    request = Request('https://deckofcardsapi.com/api/deck/{}/draw/?count=312'.format(deckID),headers = headers)
    response = urlopen(request).read()
    data = json.loads(response)
    for d in data['cards']:
        tup = (getVal(d['value']),d['image'])
        deck.append(tup)
    #print(deck)

def addCard(d,f): #removes the first card of deck array and adds it to the appropriate deck
    if len(deck) == 0:
        getNewDeck()
    if (d == playerDeck):
        d.append((deck[0][0],deck[0][1],f))
    else:
        d.append((deck[0][0],deck[0][1],f))
    deck.pop(0)

def start(): #starts the game
    global gameStatus, turn
    gameStatus = "ingame"
    turn = "player"
    #print(gameStatus + " s")
    #print(turn + " s")
    clearDeck("player")
    clearDeck("dealer")
    while len(playerDeck) < 2:
        addCard(playerDeck,"flipped")
    if len(dealerDeck) < 2:
        addCard(dealerDeck,"unflipped")
        addCard(dealerDeck,"flipped")

def clearDeck(d): #clears deck @param d
    if d == "all":
        deck.clear()
        playerDeck.clear()
        dealerDeck.clear()
    elif d == "player":
        playerDeck.clear()
    elif d == "dealer":
        dealerDeck.clear()

def getVal(card): #returns the value of @param card
    if card == "JACK" or card == "QUEEN" or card == "KING":
        return 10
    elif card == "ACE":
        return 11
    else:
        return int(card)

def getTotal(deck): #returns the total of @param deck
    val = 0
    if turn == "player" and deck == dealerDeck:
        return deck[1][0]
    for c in deck:
        val += c[0]
    return val

def dealerTurn(): #acts as the dealer
    tup = (dealerDeck[0][0],dealerDeck[0][1],"flipped")
    dealerDeck.pop(0)
    dealerDeck.insert(0, tup)
    while getTotal(dealerDeck) < 17:
        addCard(dealerDeck,"flipped")

def play(): #game rules
    global gameStatus
    #print(gameStatus)
    #print(playerDeck)
    #print(turn)
    if gameStatus == "ingame":
        #print(playerDeck)
        if turn == "player" and getTotal(playerDeck) < 21:
            addCard(playerDeck,"flipped")
            if getTotal(playerDeck) > 21: #check if total of player deck is over 21
                #print(getTotal(playerDeck))
                gameStatus = "lost"
                dbase.userInfo['coins'] -= wager
                gameStatus = "standby"
                flash("YOU LOST!")
        if turn == "dealer":
            if getTotal(dealerDeck) < 17: #while dealer has a total less than 17, keep drawing
                dealerTurn()
            if getTotal(dealerDeck) > 21: #comparing totals to determine winner
                gameStatus = "win"
                dbase.userInfo['coins'] += int(wager * 1.5)
                gameStatus = "standby"
                flash("YOU WON!")
            elif getTotal(playerDeck) == getTotal(dealerDeck):
                gameStatus = "tie"
                gameStatus = "standby"
                flash("TIE!")
            elif getTotal(playerDeck) > getTotal(dealerDeck):
                gameStatus = "win"
                dbase.userInfo['coins'] += int(wager * 1.5)
                gameStatus = "standby"
                flash("YOU WON!")
            elif getTotal(dealerDeck) > getTotal(playerDeck):
                gameStatus = "lose"
                dbase.userInfo['coins'] -= wager
                gameStatus = "standby"
                flash("YOU LOST!")
    dbase.update()

def checkBJ(): #check if player has blackjack
    if len(playerDeck) == 2 and getTotal(playerDeck) == 21:
        #print("blackjack")
        gameStatus = "win"
        dbase.userInfo['coins'] += int(2 * wager)
        gameStatus = "standby"
        flash("BLACKJACK!")

def checkBal(): #makes sure wager is not greater than balance
    if wager > dbase.userInfo['coins']:
        return False
    else:
        return True
