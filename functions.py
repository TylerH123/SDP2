from flask import Flask, render_template, flash
from urllib.request import urlopen, Request
import json
from datetime import datetime
import db as dbase

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

rolls = []
wager = 0

def getDate(): #returns date as a string in the format mm-dd-yyyy
    date = datetime.now().date() #gets the date
    date = date.strftime("%m-%d-%Y") #converts to string
    return date

def checkDate(date): #compares the difference in dates
    prevDate = date.split("-")
    nowDate = getDate().split("-")
    if int(nowDate[0]) - int(prevDate[0]) == 0 and int(nowDate[1]) - int(prevDate[1]) == 1:
        return True
    elif int(nowDate[1]) - int(prevDate[1]) > 0 or int(nowDate[0]) - int(prevDate[0]) > 1:
        return False

def getRolls(): #gets the results of 400 random rolls
    request = Request('http://roll.diceapi.com/json/400d6',headers = headers)
    response = urlopen(request).read()
    data = json.loads(response)
    for roll in data['dice']:
        rolls.append(roll['value'])

def rollDice(): #get 4 rolls and compare the sums
    global wager
    if len(rolls) < 4:
        getRolls()
    tup = (rolls[0],rolls[1],rolls[2],rolls[3])
    rolls.pop(0)
    rolls.pop(1)
    rolls.pop(2)
    rolls.pop(3)
    if int(tup[0]) + int(tup[1]) == int(tup[2]) + int(tup[3]):
        flash("Tie!")
    if int(tup[0]) + int(tup[1]) > int(tup[2]) + int(tup[3]):
        flash("You win!")
        dbase.userInfo['coins'] += int(wager * 1.5)
    elif int(tup[0]) + int(tup[1]) < int(tup[2]) + int(tup[3]):
        flash("You Lose!")
        dbase.userInfo['coins'] -= wager
    return tup
