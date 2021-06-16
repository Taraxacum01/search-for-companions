CREATE_TABLE_POSTS = """
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    isDriver TEXT,
    isType TEXT,
    idPerson INTEGER,
    idBeginPoint INTEGER,
    isEndPoint INTEGER,
    time TIMESTAMP,
    text TEXT,
    FOREIGN KEY (idPerson) REFERENCES persons (id) 
     
);
"""

CREATE_TABLE_PERSONS = """
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PPRIMARY KEY AUTOINCREMENT,
    username TEXT,
    login TEXT,
    password TEXT,
    email TEXT,
    isAdmin BOOLEAN
)
"""

CREATE_TABLE_COMMENTS = """
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PPRIMARY KEY AUTOINCREMENT,
    idPerson INTEGER,
    time TIMESTAMP,
    text TEXT
    FOREIGN KEY (idPerson) REFERENCES persons (id) 
)
"""

POSTS_QUERY = """SELECT * FROM posts"""
POST_QUERY = """SELECT * FROM posts WHERE id = ?"""

INSERT_POST_QUERY = """
INSERT INTO posts (isDriver, isType, idPerson, idBeginPoint, idEndPoint, time, text)
VALUES (?, ?, ?, ?, ?, ?, ?)
"""

DELETE_POST = """DELETE FROM posts WHERE id = ?"""

INSERT_QUERY = """
INSERT INTO posts (isDriver, isType, idPerson, idBeginPoint, idEndPoint, time, text)
VALUES ('Карточка водителя', 'type-1', 1, 1, 2, 2077-01-12, 'Я из будущего, я вас жду')
"""