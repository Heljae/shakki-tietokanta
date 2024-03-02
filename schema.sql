CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    player1_id INTEGER REFERENCES players,
    player2_id INTEGER REFERENCES players,
    elo1 INTEGER DEFAULT 0,
    elo2 INTEGER DEFAULT 0,
    event INTEGER REFERENCES tournaments,
    date DATE DEFAULT GETDATE(),
    visibility BOOLEAN
);
CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name TEXT,
    elo INTEGER DEFAULT 0,
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
    id SERIAL PRIMARY KEY,
    game_id INTEGER REFERENCES games,
    pgn TEXT
);