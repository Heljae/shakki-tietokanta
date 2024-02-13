from app import app
from flask import render_template, request, redirect
import games

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/add", methods=["POST"])
def add():
    player1 = request.form["player1"]
    player2 = request.form["player2"]
    elo1 = request.form["elo1"]  # elo (rating) during game
    elo2 = request.form["elo2"]
    event = request.form["event"]
    date = request.form["date"]
    games.add_new_game(player1, player2, int(elo1), int(elo2), event, date)
    return redirect("/")

@app.route("/print")
def print():
    all = games.get_all()
    return render_template("print.html", items=all)
