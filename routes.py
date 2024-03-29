from app import app
from flask import render_template, request, redirect
import games

@app.route("/")
def index():
    result = games.count_all()
    return render_template("index.html", games=result[0], 
                           players=result[1],
                           elo=result[2])

@app.route("/new/<int:id>")
def new(id):
    return render_template("new.html", game_id=id)

@app.route("/add/<int:id>", methods=["POST"])
def add(id):
    player1 = request.form["player1"]
    player2 = request.form["player2"]
    elo1 = request.form["elo1"]
    elo2 = request.form["elo2"]
    event = request.form["event"]
    date = request.form["date"]
    token = games.csrf_token()
    if token != request.form["csrf_token"]:
        render_template("error.html", message="virhe tiedon lähetyksessä")
    games.add_new_game(player1, player2, int(elo1), int(elo2), event, date)
    games.moves_to_db(id, player1, player2)
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
    total_games = games.count_games(id)
    all_games = games.get_player_games(id)
    return render_template("user_info.html", player=info, total=total_games, 
                           games=all_games)

@app.route("/game/<int:id>")
def game(id):
    info = games.get_game(id)
    game = info[0]
    names = info[1]
    moves = games.get_moves(id)
    if moves == None:
        message = "Valitulla pelillä ei ole siirtoja"
        return render_template("error.html", message=message)
    if info == None:
        message = "Peliä ei ole olemassa"
        return render_template("error.html", message=message)
    return render_template("game.html", game=game, players=names, moves=moves)

@app.route("/add_moves")
def add_moves():
    return render_template("moves.html")

@app.route("/post_moves", methods=["POST"])
def post_moves():
    moves = request.form["moves"]
    token = games.csrf_token()
    if token != request.form["csrf_token"]:
        render_template("error.html", message="virhe tiedon lähetyksessä")
    games.add_game_moves(moves)
    game_id = games.get_game_id(moves)
    if moves == "":
        message = "Pelillä täytyy olla siirrot!"
        return render_template("error.html", message=message)
    return render_template("new.html", game_id=game_id)

@app.route("/find_games", methods=["GET","POST"])
def find_player():
    if request.method == "GET":
        return render_template("search_games.html")
    if request.method == "POST":
        name = request.form["name"]
        token = games.csrf_token()
        if token != request.form["csrf_token"]:
            render_template("error.html", message="virhe tiedon lähetyksessä")
        player_id = games.find_player(name)
        if player_id != None:
            return redirect(f"/user_info/{player_id}")
        else:
            message = "Pelaajaa ei löytynyt"
            return render_template("error.html", message=message)