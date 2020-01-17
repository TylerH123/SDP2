# Baguette Grabbers
Welcome to the Gambling Den!

This is a site where users can play many different games, such as blackjack, roulette, slots, broccoli clicker, sudoku. Blackjack, roulette, and slots will cost coins to play. Users can gain coins by logging in everyday, playing broccoli clicker, or winning a sudoku puzzle.

### Roster:
- Tyler: Project Manager/database
- William: Frontend CSS
- Ethan: Backend Flask
- Jionghao: Backend Flask


### APIs required (no keys needed!!!):
- [Deck of Cards](https://docs.google.com/document/d/1oCJhl-NoNNpekMLd4C4jBXhpL9xvm6ZrVIdfoqbq-Vc/edit) - create games that requires the usage of a deck of cards (Blackjack)
- [Sudoku](https://docs.google.com/document/d/14Lw3HV3ViifQ-goOmka-vE_yt3o_YpcJIjgnqRbF4ds/edit#heading=h.e1qrjd4103ct) - use a template of sudoku games for one of our minigames
- [Diceful](https://docs.google.com/document/d/1pvPPwTMcXs1OyTqh5QbucGXou4OOnOis5HjtIT90W5w/edit) - create games that requires the usage of dice (Roulette, Craps)
- [video demo here](https://youtu.be/X6QNdORJPPA)


### How to run this project
1. To ensure that we're running on the same package versions, run it with a virtual environment with the following commands:
   ```
   python3 -m venv <name of vitrual environment>    # creates a virtual environment named <name of virtual environment>
   .<name of vitrual environment>/bin/activate      # activates the virtual environment
   ```
2. Clone and change into our repository:
   ```
   git clone https://github.com/TylerH123/SDP2.git
   cd SDP2/
   ```
3. Install all the needed packages using the following command in a terminal: <br>
   ```
   pip3 install -r doc/requirements.txt
   ```
4. Once all the packages are install, reset the database to make sure all tables are correct:
   ```
   python3 reset.py
   ```
   Then run the project:
   ```
   python3 app.py
   ```
   Once the Flask is running, open http://127.0.0.1:5000/ in the browser

5. If you are running a virtual environment, deactivate it by entering `deactivate` into the command line.
