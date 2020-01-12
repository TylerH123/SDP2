#Team Baguette Grabbers
#huangT, chenE, linW, wuJ
#SoftDev1 pd2
#P #02: The End
#2019-1-16

from flask import Flask, render_template, request,  session, redirect, url_for, flash, Response
import sqlite3
import urllib, json
import db as dbase  #helper functions found in db.py
import functions as func
import blackjack as bj
app = Flask(__name__)
app.secret_key = "adsfgt"

session = {}

@app.route("/") #Initally loaded page
def root():
    if 'user' in session:
        return redirect(url_for("home"))
    else:
        return render_template("index.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    return render_template("login.html")

@app.route("/register", methods = ["POST", "GET"])
def register():
    return render_template("register.html")

@app.route("/update", methods = ["POST", "GET"]) #The page accessed to update your own data
def update():
    return render_template("update.html")

@app.route("/auth", methods = ["POST"]) #This route authenticates registration and log in, and other updates
def auth():
    if request.form['submit_button'] == "Sign me up": #If you were sent here by registering
        if dbase.addUser():
            return redirect(url_for("root"))
        else:
            return redirect(url_for("register")) #if addUser() returns false, it will also handle flashing the correct error message
    if request.form['submit_button'] == "Login": #if sent here by logging in
        if dbase.login():
            session['user'] = request.form['username'] #stores the user in the session
            return redirect(url_for("home"))
        else:
            return redirect(url_for("login"))
    if request.form['submit_button'] == "Update Info": #If updating info, fill in db
        dbase.updatePass()
        return redirect(url_for("home"))
    if request.form['submit_button'] == "Update Key" or request.form['submit_button'] == "Add Key":
        dbase.updateAPIKey(request.form['submit_button'])
        return redirect(url_for("home"))

@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user')
        dbase.update()
        dbase.userID = -1
        bj.clearDeck("all")
    flash("Logout Success!")
    flash("index")
    return redirect(url_for("root"))

@app.route("/home", methods = ['POST','GET'])
def home(): #display home page of website
    if 'user' in session:
        # read json + reply
        bj.clearDeck("player")
        bj.clearDeck("dealer")
        return render_template("homepage.html",
                                coins = dbase.userInfo['coins'],
                                timeStmp = dbase.userInfo['timeStmp'],
                                streak = dbase.userInfo['streak'])
    else:
        return redirect(url_for("root"))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/howToUse")
def howToUse():
    return render_template("howToUse.html")

#@app.route("/dice", methods=['POST'])
#def dice():
#    data = request.json
#    win = func.checkDiceWin(data)
#    if (win):
#        dbase.userInfo['coins'] += 100;
#    else:
#        dbase.userInfo['coins'] -= 100;
#    return redirect(url_for("home"))

@app.route("/blackjack")
def blackjack():
    if 'user' in session:
        return render_template("blackjack.html",
                                coins = dbase.userInfo['coins'],
                                deck = bj.deck,
                                cards = bj.playerDeck,
                                dcards = bj.dealerDeck,
                                total = bj.getTotal(bj.playerDeck),
                                dtotal = bj.getTotal(bj.dealerDeck))
    else:
        return redirect(url_for("root"))

@app.route("/blackjack/loadDeck")
def loadDeck():
    if len(bj.deck) == 0:
        bj.getNewDeck()
    bj.start()
    bj.checkBJ()
    bj.wager = int(request.args['wager'])
    return redirect(url_for("blackjack"))

@app.route("/blackjack/hit")
def hit():
    if bj.turn == "player":
        bj.play()
    return redirect(url_for("blackjack"))


@app.route("/blackjack/fold")
def fold():
    bj.turn = "dealer"
    bj.dealerTurn()
    if bj.gameStatus == "ingame":
        bj.play()
    return redirect(url_for("blackjack"))

@app.route("/blackjack/stand")
def stand():
    bj.turn = "dealer"
    bj.play()
    return redirect(url_for("blackjack"))

@app.route("/blackjack/reset")
def bjReset():
    if bj.gameStatus == "standby":
        bj.start()
        bj.checkBJ()
        #print(bj.getTotal(bj.playerDeck))
    return redirect(url_for("blackjack"))

@app.route("/blackjack/bjstart")
def bjStart():
    if 'user' in session:
        return render_template("bjStart.html", coins = dbase.userInfo['coins'])
    else:
        return redirect(url_for("root"))

@app.route("/wheel")
def wheel():
    return render_template("wheel.html")

@app.route("/craps")
def craps():
    if 'user' in session:
        return render_template("craps.html")
    else:
        return redirect(url_for("root"))

if __name__ == "__main__":
    app.debug = True
    app.run()
