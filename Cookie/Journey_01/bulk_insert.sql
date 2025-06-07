DROP TABLE IF EXISTS heros;
DROP TABLE IF EXISTS encounters;

CREATE TABLE heros (
    c_id INTEGER PRIMARY KEY,
    c_name TEXT NOT NULL,
    c_wit INTEGER, 
    c_strength INTEGER, 
    c_attack INTEGER, 
    c_defense INTEGER,
    c_magic INTEGER
);

INSERT INTO characters 
(c_id, c_name, c_wit, c_strength, c_attack, c_defense, c_magic)
VALUES
(0, "Archibald", 0, 7, 2, 1, 0),
(1, "Henrik", 4, 3, 3, 1, 2),
(2, "Isadore", 2, 6, 4, 0, 4),
(3, "Lucinda", 4, 3, 1, 8, 1),
(4, "Dominic", 5, 2, 3, 3, 2);