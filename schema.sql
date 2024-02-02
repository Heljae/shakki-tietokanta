CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    player1_id TEXT,
    palyer2_id TEXT,
    elo1 INTEGER,
    elo2 INTEGER,
    event TEXT,
    date DATETIME
);
CREATE TABLE players {
    id SERIAL PRIMARY KEY,
    name TEXT,
    elo INTEGER
};
CREATE TABLE tournaments {
    id SERIAL PRIMARY KEY,
    game_id
}