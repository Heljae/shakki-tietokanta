CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    player1_id INTEGER REFERENCES players,
    palyer2_id INTEGER REFERENCES players,
    elo1 INTEGER,
    elo2 INTEGER,
    event TEXT,
    date TEXT
);
CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name TEXT,
    elo INTEGER
);
CREATE TABLE tournaments (
    id SERIAL PRIMARY KEY,
    game_id INTEGER REFERENCES games
);