from db import db
from sqlalchemy.sql import text

def check_player(name):
    """Checks if a player is in the database
    """

    sql = text("SELECT name FROM Players WHERE name=:name;")
    value = db.session.execute(sql, {"name":name}).fetchone()
    if value == None:
        return False
    return True

def tournament_checker(name):
    """Checks if tournament in in the database
    """

    sql = text("SELECT name FROM tournaments WHERE name=:name")
    tournament = db.session.execute(sql, {"name":name}).fetchone()
    if tournament == None:
        return False
    return True

def add_player(name, elo):
    """Adds a player into the database
    """

    sql = text("INSERT INTO Players (name, elo) VALUES (:name, :elo);")
    db.session.execute(sql, {"name":name, "elo":elo})

def add_event(name):
    """Adds a tournament into the database
    """

    sql = text("INSERT INTO tournaments (name) VALUES (:name);")
    db.session.execute(sql, {"name":str(name)})
    db.session.commit()

def get_player_id(name):
    """Gets the player id for the given name
    """

    sql = text("SELECT id FROM players WHERE name=:name;")
    id = db.session.execute(sql, {"name":name}).fetchone()[0]
    return id

def moves_to_list(moves:str):
    """Turns a string of moves into a list
    """
    move_list = moves.split()
    all = []
    help = 0
    new = ""
    for move in move_list:
        if help == 3:
            all.append(new)
            new = ""
            help = 0
        new += move+" "
        help += 1
    if new != "":
        all.append(new)
    return all

def player_info(player_id):
    sql = text("SELECT * FROM players WHERE id=:id")
    info = db.session.execute(sql, {"id":player_id}).fetchone()
    return info

def get_games_info(player_id):
    """Gets the info of all the games of a player
    """
    sql2 = text("SELECT * FROM games WHERE player1_id=:player_id \
               OR player2_id=:player_id")
    games = db.session.execute(sql2, {"player_id":player_id}).fetchall()
    total = []
    for game in games:
        game_info = {}
        player1 = player_info(game.player1_id)
        player2 = player_info(game.player2_id)
        game_info["player1"] = player1.name
        game_info["player2"] = player2.name
        game_info["elo1"] = game.elo1
        game_info["elo2"] = game.elo2
        game_info["event"] = game.event
        game_info["date"] = game.date
        total.append(game_info)
    return total

