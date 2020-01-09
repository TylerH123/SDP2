from flask import Flask, render_template, request,  session, redirect, url_for, flash
import sqlite3 # enable control of an sqlite database

userID = -1
userInfo = {}

def addUser(): #adds user to database
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
                c.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?);", (id, request.form['username'], request.form['password'], 0.0, 0, "01-08-2020", "False")) #different version of format
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
                return True
            else:
                flash("Error! Incorrect password")
                return False
    else:
        flash("Error! Username does not exist")
        return False

def updatePass(): #updates a user's password
    dbfile = "data.db"
    db = sqlite3.connect(dbfile)
    c = db.cursor()
    blank = True
    if request.form['password'] != "":
        command = "UPDATE users SET {} = \"{}\" WHERE id = {};"
        c.execute(command.format('password',request.form['password'],userID))
        blank = False
        db.commit()
    if not blank:
        flash("Update Success!")
    else:
        flash("Nothing has been updated.")
    db.commit()
    db.close()

def update(): #updates a user's info
    dbfile = "data.db"
    db = sqlite3.connect(dbfile)
    c = db.cursor()
    arr = ['coins','streak','timeStmp','daily']
    idx = 0
    while idx < len(arr):
        command = "UPDATE users SET {} = \"{}\" WHERE id = {};"
        c.execute(command.format(arr[idx],userInfo[arr[idx]],userID))
        db.commit()
        idx += 1
    db.commit()
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
        userInfo['daily'] = bar[6]
