CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    player1_id INTEGER,
    player2_id INTEGER,
    elo1 INTEGER,
    elo2 INTEGER,
    event TEXT,
    date DATE,
    visibility BOOLEAN
);
CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name TEXT,
    elo INTEGER,
    club TEXT
);
CREATE TABLE tournaments (
    id SERIAL PRIMARY KEY,
    name TEXT,
    place TEXT,
    time TEXT
);
CREATE TABLE clubs (
    id SERIAL PRIMARY KEY,
    name TEXT
);
CREATE TABLE moves (
    id SERIAL PRIMARY KEY,
    game_id INTEGER,
    pgn TEXT
);