headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

import os
from flask import Flask, render_template
from urllib.request import urlopen, Request
import json
from datetime import datetime
now = datetime. now(). time()
print("now =", now)
print("type(now) =", type(now))
test = Flask(__name__)
test.secret_key = os.urandom(32)

def card():
    request = Request('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1',headers = headers)
    response = urlopen(request).read()
    data = json.loads(response)
    return(data['deck_id'])

@test.route('/sudoku')
def sudoku():
    request = Request('http://www.cs.utep.edu/cheon/ws/sudoku/new/?size=9&level=1',headers = headers)
    response = urlopen(request).read()
    data = json.loads(response)
    board = makeBoard(data['squares'])
    return render_template('sudoku.html', board = board)

def makeBoard(squares):
    board = [[0 for i in range(9)] for j in range(9)] #makes a default 4x4 2-d array with only 0 for values
    for square in squares:
        board[square['x']][square['y']] = square['value']
    print(board)
    return board

if __name__ == "__main__":
    #db_builder.db_build()
    test.debug = True
    test.run()
