from flask import Flask, request, flash
import sqlite3 # enable control of an sqlite database
import functions as func

userID = -1
userInfo = {}

def addUser(): #adds user to da tabase
    if request.form['password'] != request.form['password2']:
        flash("Error! Passwords do not match")
        return False
    else:
        dbfile = "data.db"
        db = sqlite3.connect(dbfile)
        c = db.cursor() #standard connection
        command = "SELECT COUNT(*) FROM users WHERE username = \"{}\";"
        newUser = c.execute(command.format(request.form['username'])) #execution of sqlite command with the given username instead of the brackets
        for bar in newUser:
            if bar[0] > 0: #if username exists
                flash("Username is already taken. Please choose another one.")
                return False
            else:
                id = getTableLen("users") #gives the user the next availabe id
                c.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?);", (id, request.form['username'], request.form['password'], 0, 0, "new", 1)) #different version of format
                db.commit()
                db.close()
                flash("Register Success!")
                flash("index")
                return True

def login(): #login function
    global userID
    dbfile = "data.db"
    db = sqlite3.connect(dbfile)
    c = db.cursor()
    command = "SELECT * FROM users WHERE username = \"{}\";"
    listUsers = c.execute(command.format(request.form['username'])) #fills in brackets with the given username and executes it in sqlite
    bar = list(enumerate(listUsers))
    if len(bar) > 0: #checks whether there exists a user with the given username
        getPass = "SELECT password FROM users WHERE username = \"{}\";"
        listPass = c.execute(getPass.format(bar[0][1][1]))
        for p in listPass:
            if request.form['password'] == p[0]: #compare passwords
                userID = bar[0][1][0]
                fillUserInfo()
                checkDaily()
                update()
                return True
            else:
                flash("Error! Incorrect password")
                return False
    else:
        flash("Error! Username does not exist")
        return False

def update(): #updates a user's info
    dbfile = "data.db"
    db = sqlite3.connect(dbfile)
    c = db.cursor()
    arr = ['coins','streak','timeStmp','farmLvl']
    idx = 0
    while idx < len(arr):
        command = "UPDATE users SET {} = \"{}\" WHERE id = {};"
        c.execute(command.format(arr[idx],userInfo[arr[idx]],userID))
        db.commit()
        idx += 1
    db.close()

def getInfo(game,info): #get the specified info for a given game
    dbfile = "data.db"
    db = sqlite3.connect(dbfile)
    c = db.cursor()
    command = "SELECT {} FROM info WHERE gameName = \"{}\";"
    inf = c.execute(command.format(info,game))
    for target in inf:
        return target[0]

def getTableLen(tbl): #returns the length of a table
    dbfile = "data.db"
    db = sqlite3.connect(dbfile)
    c = db.cursor()
    command = "SELECT COUNT(*) FROM {};"
    q = c.execute(command.format(tbl))
    for line in q:
        return line[0]

def fillUserInfo(): #fills userInfo with info on the current user
    dbfile = "data.db"
    db = sqlite3.connect(dbfile)
    c = db.cursor()
    q = c.execute("SELECT * FROM users WHERE id = {};".format(userID))
    for bar in q:
        userInfo['username'] = bar[1]
        userInfo['coins'] = bar[3]
        userInfo['streak'] = bar[4]
        userInfo['timeStmp'] = bar[5]
        userInfo['farmLvl'] = bar[6]

def checkDaily(): #check to see if eligible for daily reward
    if userInfo['timeStmp'] == "new" or userInfo['streak'] == 0 or func.checkDate(userInfo['timeStmp']):
        userInfo['streak'] += 1
        userInfo['coins'] += 500
    elif func.checkDate(userInfo['timeStmp']) == 2:
        userInfo['streak'] = 0
    userInfo['timeStmp'] = func.getDate()
