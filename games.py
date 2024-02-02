from db import db

def add_new_game(player1, player2, elo1, elo2, event, date):
    player1_id = db.session.execute("""
    SELECT IFNULL(id, 0)
    FROM Players WHERE name=:name""", player1)

    player2_id = db.session.execute("""
    SELECT IFNULL(id, 0)
    FROM Players WHERE name=:name""", player2)

    if player1_id == 0:
        sql1 = "INSERT INTO Players (name, elo) VALUES (:player1, :elo1)"
        db.session.execute(sql1, {"name":player1, "elo":elo1})
        player1_id = db.session.execute("""SELECT * FROM Players
                                       ORDER BY id DESC LIMIT 1""")
    if player2_id == 0:
        sql1 = "INSERT INTO Players (name, elo) VALUES (:player1, :elo1)"
        db.session.execute(sql1, {"name":player1, "elo":elo1})
        player2_id = db.session.execute("""SELECT * FROM Players
                                       ORDER BY id DESC LIMIT 1""")

    sql = """INSERT INTO Games 
    (player1, player2, elo1, elo2, event, date)
    VALUES (:player1, :player2, :elo1, :elo2, :event, :date)
    RETURNING id"""
    db.session.execute(sql, {"player1":player1_id, "player":player2_id,
                            "elo1":elo1, "elo2":elo2,
                            "event":event, "date":date})
    db.session.commit()
    return True

# TODO:
    # adding players separately into db