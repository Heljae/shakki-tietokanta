from db import db
from sqlalchemy.sql import text

def add_new_game(player1, player2, elo1, elo2, event, date):
    # if player1_id == 0:
    #     sql1 = "INSERT INTO Players (name, elo) VALUES (:player1, :elo1)"
    #     db.session.execute(sql1, {"name":player1, "elo":elo1})
    #     player1_id = db.session.execute("SELECT * FROM Players ORDER BY id DESC LIMIT 1").fetchone()[0]
    # if player2_id == 0:
    #     sql2 = "INSERT INTO Players (name, elo) VALUES (:player2, :elo2)"
    #     db.session.execute(sql2, {"name":player2, "elo":elo2})
    #     player2_id = db.session.execute("SELECT * FROM Players ORDER BY id DESC LIMIT 1").fetchone()[0]

    db.session.execute(text("INSERT INTO players (name,elo) VALUES (:name, :elo);"),{"name":"jee","elo":1400})
    db.session.execute(text("INSERT INTO players (name,elo) VALUES (:name, :elo);"),{"name":"moi","elo":1800})

    player1_id = db.session.execute(text("SELECT id FROM players WHERE name=:name;"), {"name":"jee"}).fetchone()[0]
    player2_id = db.session.execute(text("SELECT id FROM players WHERE name=:name;"), {"name":"moi"}).fetchone()[0]

    sql = text("INSERT INTO Games (player1_id, palyer2_id, elo1, elo2, event, date) VALUES (:player1, :player2, :elo1, :elo2, :event, :date)")
    db.session.execute(sql, {"player1":player1_id, "player2":player2_id,
                            "elo1":elo1, "elo2":elo2,
                            "event":event, "date":date})
    db.session.commit()

def get_all():
    sql = text("SELECT * FROM games")
    games = db.session.execute(sql).fetchall()

    db.session.commit()
    return games


