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

def add_player(name, elo):
    """Adds a player into the database
    """

    sql = text("INSERT INTO Players (name, elo) VALUES (:name, :elo);")
    db.session.execute(sql, {"name":name, "elo":elo})