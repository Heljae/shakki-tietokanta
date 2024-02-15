CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    player1_id INTEGER REFERENCES players,
    player2_id INTEGER REFERENCES players,
    elo1 INTEGER,
    elo2 INTEGER,
    event INTEGER REFERENCES tournaments,
    date TEXT,
    visibility BOOLEAN
);
CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name TEXT,
    elo INTEGER,
    club TEXT REFERENCES clubs
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
    game_id INTEGER REFERENCES games,
    pgn TEXT
);