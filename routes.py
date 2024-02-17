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

@app.route("/print_games")
def print_games():
    all = games.get_all()
    return render_template("print_games.html", games=all)

@app.route("/list_players")
def list_players():
    all = games.get_players()
    return render_template("list_players.html", players=all)

@app.route("/user_info/<int:id>")
def user_info(id):
    info = games.player_info(id)
    return render_template("user_info.html", player=info)

@app.route("/game/<int:id>")
def game(id):
    info = games.get_game(id)
    game = info[0]
    names = info[1]
    return render_template("game.html", game=game, players=names)
