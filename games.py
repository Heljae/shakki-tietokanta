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

    sql = text("INSERT INTO Games (player1_id, player2_id, elo1, elo2, event, date) \
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
        name2 = db.session.execute(sql3, {"id":row.player2_id}).fetchone()[0]

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
    player2 = player_info(info.player2_id)
    players = [player1, player2]
    return info, players

def add_game_moves(moves):
    """Adds moves of a game to the database
    """
    sql = text("INSERT INTO moves (pgn) VALUES (:moves);")
    db.session.execute(sql, {"moves":moves})
    db.session.commit()

def get_game_id(moves):
    """Gets game id based on moves.
    """
    sql = text("SELECT id FROM moves WHERE pgn=:pgn;")
    game_id = db.session.execute(sql, {"pgn":str(moves)}).fetchone()[0]
    return game_id

def moves_to_db(id, player1, player2):
    """Posts the moves to the db.
    """
    sql = text("SELECT id FROM games WHERE player1_id=:player1 AND player2_id=:player2")
    id1 = game_manager.get_player_id(player1)
    id2 = game_manager.get_player_id(player2)
    game_id = db.session.execute(sql, {"player1":id1, "player2":id2}).fetchone()[0]

    sql2 = text("UPDATE moves SET game_id=:game_id WHERE id=:id;")
    db.session.execute(sql2, {"game_id":game_id, "id":id})
    db.session.commit()

def get_moves(game_id):
    """Gets the moves of a game from game_id
    """
    sql = text("SELECT pgn FROM moves WHERE game_id=:game_id")
    moves = db.session.execute(sql, {"game_id":game_id}).fetchone()[0]
    return game_manager.moves_to_list(moves)

def count_games(player_id):
    """Counts all of the games from the given player
    """

    sql = text("SELECT COUNT(*) FROM games \
               WHERE player1_id=:player1_id OR player2_id=:player2_id")
    count = db.session.execute(sql, {"player1_id":player_id, \
                                     "player2_id":player_id}).fetchone()

    return count[0]

def find_player(name):
    """Finds the info of a player by name
    """
    player_id = game_manager.get_player_id(name)
    return player_id

def get_player_games(player_id):
    """Gets all of a players games
    """
    games = game_manager.get_games_info(player_id)
    return games

def count_all():
    """Counts all games
    """
    sql = text("SELECT COUNT(DISTINCT id) \
               FROM games")
    games = db.session.execute(sql).fetchone()[0]

    sql2 = text("SELECT COUNT(DISTINCT id) \
                FROM players")
    players = db.session.execute(sql2).fetchone()[0]

    sql3 = text("SELECT SUM(elo)/COUNT(id) \
                FROM players")
    average = db.session.execute(sql3).fetchone()[0]
    return games, players, average
