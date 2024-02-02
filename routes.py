from app import app
from flask import render_template, request, redirect
import games

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new", methods=["POST"])
def new():
    player1 = request.form["player1"]
    player2 = request.form["player2"]
    elo1 = request.form["elo1"]  # elo (rating) during game
    elo2 = request.form["elo2"]
    event = request.form["event"]
    date = request.form["date"]
    game = games.add_new_game(player1, player2, elo1, elo2, event, date)
    if not game:
        pass   # todo
    return redirect("/")