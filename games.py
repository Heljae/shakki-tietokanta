from db import db
from sqlalchemy.sql import text
import handling_info

def add_new_game(player1, player2, elo1, elo2, event, date):
    """Adds a new game to the database
    """
    # db.session.execute(text("INSERT INTO players (name,elo) \
    #                         VALUES (:name, :elo);"),{"name":"jee","elo":1400})
    # db.session.execute(text("INSERT INTO players (name,elo) \
    #                         VALUES (:name, :elo);"),{"name":"moi","elo":1800})

    if not handling_info.check_player(player1):
        handling_info.add_player(player1, elo1)

    if not handling_info.check_player(player2):
        handling_info.add_player(player2, elo2)

    player1_id = db.session.execute(text("SELECT id FROM players \
                                         WHERE name=:name;"), {"name":player1}).fetchone()[0]
    player2_id = db.session.execute(text("SELECT id FROM players \
                                         WHERE name=:name;"), {"name":player2}).fetchone()[0]

    sql = text("INSERT INTO Games (player1_id, palyer2_id, elo1, elo2, event, date) \
               VALUES (:player1, :player2, :elo1, :elo2, :event, :date)")
    
    db.session.execute(sql, {"player1":player1_id, "player2":player2_id,
                            "elo1":elo1, "elo2":elo2,
                            "event":event, "date":date})
    db.session.commit()

def get_all():
    sql = text("SELECT * FROM games")
    games = db.session.execute(sql).fetchall()

    game_info = []

    for row in games:
        game = list(row)
        sql2 = text("SELECT name FROM Players WHERE id=:id;")
        name1 = db.session.execute(sql2, {"id":game[1]}).fetchone()[0]
        game[1] = name1

        sql3 = text("SELECT name FROM Players WHERE id=:id;")
        name2 = db.session.execute(sql3, {"id":game[2]}).fetchone()[0]
        game[2] = name2

        game_info.append(game)

    db.session.commit()

    return game_info


