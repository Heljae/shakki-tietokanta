import games
from db import db
from sqlalchemy.sql import text

def add_existing_games():
    pgn = "1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Bd3 c5 6. Ne2 d5 7. a3 Bxc3+ 8. bxc3 dxc4 9. Bxc4 Qc7 10. Ba2 b6 11. O-O Ba6 12. Bb2 Nc6 13. Rc1 Rac8 14. c4 cxd4 15. exd4 Qe7 16. d5 exd5 17. Re1 Bxc4 18. Ng3 Qd8 19. Bb1 b5 20. Nf5 d4 21. Qd2 Be6 22. Rc5 a6 23. Nxg7 Kxg7 24. Qg5+ Kh8 25. Qh4 Rg8 26. Rxc6 Rxc6 27. Bxd4 Kg7 28. Qxh7+ Kf8 29. Qh6+ Ke8 30. Bxf6 Qa5 31. Qe3 Qb6 32. Rd1 Rd6 33. Bd4 Qc6 34. Be4 Qc4 35. h3 Kd7 36. Rd2 Re8 37. Kh2 Bd5 38. Bf5+ Be6 39. Bd3 Qa4 40. Be5 Rd5 41. Qa7+ 1-0"
    player1 = "Carlsen, Magnus"
    player2 = "Nakamura, Hikaru"
    elo1 = 2863
    elo2 = 2736
    event = "Carlsen Tour Final"
    date = "2020-08-19"

    sql = text("SELECT id FROM games WHERE elo1=:elo1 AND elo2=elo2")
    game_id = db.session.execute(sql, {"elo1":elo1, "elo2":elo2})

    games.moves_to_db(game_id, player1, player2)
    games.add_new_game(player1, player2, elo1, elo2, event, date)

    pgn1 = "1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. f3 e5 7. Nb3 Be6 8. Be3 Be7 9. Qd2 O-O 10. O-O-O Nbd7 11. g4 b5 12. Rg1 Nb6 13. Na5 Rc8 14. g5 Nh5 15. Kb1 Qc7 16. Nd5 Nxd5 17. exd5 Bxd5 18. Qxd5 Qxa5 19. Bd3 g6 20. c4 Nf4 21. Bxf4 exf4 22. cxb5 axb5 23. Qxb5 Qa7 24. Be4 Rc7 25. Bd5 Qf2 26. Qb3 Qxh2 27. a4 Qf2 28. Rc1 Ra7 29. Qb4 Qe3 30. Rcd1 Qe5 31. Qb5 Kg7 32. Bc6 Rc8 33. Rg2 d5 34. Bxd5 Rc5 35. Qb3 Bxg5 36. Bc4 Bf6 37. Re2 Qf5+ 38. Re4 Re5 39. Re1 Rxe4 40. Rxe4 Re7 41. Bd3 Rxe4 42. Bxe4 Qd7 43. Qb5 Qxb5 44. axb5 Bd4 45. Kc2 h5 46. b6 Bxb6 47. Kd1 f5 48. Bc6 g5 49. Bd7 Kf6 50. Ke2 g4 51. Kf1 Kg5 0-1"
    player11 = "Caruana, Fabiano"
    player21 = "Vachier-Lagrave, Maxime"
    elo11 = 2844
    elo21 = 2757
    event1 = "Tashkent FIDE GP 2014"
    date1 = "2014-10-21"

    sql1 = text("SELECT id FROM games WHERE elo1=:elo1 AND elo2=elo2")
    game_id1 = db.session.execute(sql1, {"elo1":elo11, "elo2":elo21})

    games.moves_to_db(game_id1, player11, player21)
    games.add_new_game(player11, player21, elo11, elo21, event1, date1)

    pgn2 = "1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. d3 b5 6. Bb3 Bc5 7. Nc3 O-O 8. Nd5 Nxd5 9. Bxd5 Rb8 10. O-O Ne7 11. Nxe5 Nxd5 12. exd5 Re8 13. d4 Bf8 14. b3 Bb7 15. c4 d6 16. Nf3 Qf6 17. Be3 Bc8 18. Qd2 Qg6 19. Kh1 h6 20. Rac1 Be7 21. Ng1 Bg5 22. Bxg5 Qxg5 23. Rfd1 bxc4 24. bxc4 Qxd2 25. Rxd2 a5 26. h3 Rb4 27. Nf3 Bf5 28. c5 Kf8 29. Nh2 Reb8 30. Ng4 Rb1 31. Rxb1 Rxb1+ 32. Kh2 a4 33. Ne3 Bg6 34. Kg3 Rb4 35. Kf3 Ke7 36. Ke2 Kd7 37. f3 Rb5 38. Nd1 Rb4 39. c6+ Kc8 40. Nc3 f6 41. Ke3 Rc4 42. Ne2 a3 43. h4 Rb4 44. g4 Rb1 45. h5 Bh7 46. f4 f5 47. g5 Rh1 48. Ng3 Rh3 49. Kf3 hxg5 50. fxg5 g6 51. Re2 Kd8 52. hxg6 Bxg6 53. Re6 Bf7 54. g6 Bg8 55. g7 f4 56. Kxf4 Rh2 57. Nf5 Rxa2 58. Rf6 Re2 59. Rf8+ 1-0"
    player12 = "Carlsen, Magnus"
    player22 = "Aronian, Levon"
    elo12 = 2848
    elo22 = 2815
    event2 = "London Classic 4th"
    date2 = "2012-12-02"

    sql2 = text("SELECT id FROM games WHERE elo1=:elo1 AND elo2=elo2")
    game_id2 = db.session.execute(sql2, {"elo1":elo12, "elo2":elo22})

    games.moves_to_db(game_id2, player12, player22)
    games.add_new_game(player12, player22, elo12, elo22, event2, date2)

    db.session.commit()    
