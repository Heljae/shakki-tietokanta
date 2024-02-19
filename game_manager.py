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
