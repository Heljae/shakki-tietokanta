from db import db
from sqlalchemy.sql import text
import game_manager

def add_new_game(player1, player2, elo1, elo2, event, date):
    """Adds a new game to the database
    """

    if not game_manager.check_player(player1):
        game_manager.add_player(player1, elo1)

    if not game_manager.check_player(player2):
        game_manager.add_player(player2, elo2)

    if not game_manager.tournament_checker(event):
        game_manager.add_event(event)

    player1_id = game_manager.get_player_id(player1)
    player2_id = game_manager.get_player_id(player2)

    sql = text("INSERT INTO Games (player1_id, palyer2_id, elo1, elo2, event, date) \
               VALUES (:player1, :player2, :elo1, :elo2, :event, :date)")
    
    db.session.execute(sql, {"player1":player1_id, "player2":player2_id,
                            "elo1":elo1, "elo2":elo2,
                            "event":event, "date":date})
    db.session.commit()

def get_all():
    sql = text("SELECT * FROM games")
    games = db.session.execute(sql).fetchall()

    game_info = {}

    for row in games:
        sql2 = text("SELECT name FROM Players WHERE id=:id;")
        name1 = db.session.execute(sql2, {"id":row.player1_id}).fetchone()[0]

        sql3 = text("SELECT name FROM Players WHERE id=:id;")
        name2 = db.session.execute(sql3, {"id":row.palyer2_id}).fetchone()[0]

        game_info[row.id] = (row, [name1, name2])

    return game_info

def get_players():
    """Returns a list of all the players
    """

    sql = text("SELECT * FROM players ORDER BY elo DESC")
    players = list(db.session.execute(sql))
    db.session.commit()
    all = []
    for i in range(1, len(players)+1):
        all.append([i]+list(players[i-1]))
    return all

def player_info(player_id):
    """Gets the player info for a specific player
    """

    sql = text("SELECT * FROM players WHERE id=:id")
    info = db.session.execute(sql, {"id":player_id}).fetchone()
    return info

def get_game(game_id):
    """Gets all of certain game's info
    """

    sql = text("SELECT * FROM games WHERE id=:id;")
    info = db.session.execute(sql, {"id":game_id}).fetchone()
    player1 = player_info(info.player1_id)
    player2 = player_info(info.palyer2_id)
    players = [player1, player2]
    return info, players
