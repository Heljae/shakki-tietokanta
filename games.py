from db import db

def add_new_game(player1, player2, elo1, elo2, event, date):
    player1_id = db.session.execute("SELECT id FROM Players WHERE name=:name", {"name":player1}).fetchone()[0] or 0

    player2_id = db.session.execute("SELECT id FROM Players WHERE name=:name", {"name":player2}).fetchone()[0] or 0

    if player1_id == 0:
        sql1 = "INSERT INTO Players (name, elo) VALUES (:player1, :elo1)"
        db.session.execute(sql1, {"name":player1, "elo":elo1})
        player1_id = db.session.execute("SELECT * FROM Players ORDER BY id DESC LIMIT 1").fetchone()[0]
    if player2_id == 0:
        sql2 = "INSERT INTO Players (name, elo) VALUES (:player2, :elo2)"
        db.session.execute(sql2, {"name":player2, "elo":elo2})
        player2_id = db.session.execute("SELECT * FROM Players ORDER BY id DESC LIMIT 1").fetchone()[0]

    sql = "INSERT INTO Games (player1, player2, elo1, elo2, event, date) VALUES (:player1, :player2, :elo1, :elo2, :event, :date)"
    db.session.execute(sql, {"player1":player1_id, "player2":player2_id,
                            "elo1":elo1, "elo2":elo2,
                            "event":event, "date":date})
    db.session.commit()

