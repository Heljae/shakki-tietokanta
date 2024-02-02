CREATE TABLE Games (
    id SERIAL PRIMARY KEY,
    player1_id INTEGER REFERENCES Players,
    palyer2_id INTEGER REFERENCES Players,
    elo1 INTEGER,
    elo2 INTEGER,
    event TEXT,
    date DATETIME
);
CREATE TABLE Players {
    id SERIAL PRIMARY KEY,
    name TEXT,
    elo INTEGER
};
CREATE TABLE Tournaments {
    id SERIAL PRIMARY KEY,
    game_id
}