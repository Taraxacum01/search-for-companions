CREATE_TABLE_POSTS = """
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    isDriver TEXT,
    isType TEXT,
    idPerson INTEGER,
    idBeginPoint INTEGER,
    idEndPoint INTEGER,
    time DATETIME DEFAULT CURRENT_TIMESTAMP,
    text TEXT,
    FOREIGN KEY (idPerson) REFERENCES persons (id) 
     
);
"""

POSTS_QUERY = """SELECT * FROM posts"""
POST_QUERY = """SELECT * FROM posts WHERE id = ?"""

INSERT_POST_QUERY = """
INSERT INTO posts (isDriver, isType, idPerson, idBeginPoint, idEndPoint, text)
VALUES (?, ?, ?, ?, ?, ?)
"""

DELETE_POST = """DELETE FROM posts WHERE id = ?"""

INSERT_QUERY = """
INSERT INTO posts (isDriver, isType, idPerson, idBeginPoint, idEndPoint, text)
VALUES ('Карточка водителя', 'type-1', 1, 1, 2, 'Я из будущего, я вас жду')
"""
################################################################

CREATE_TABLE_PERSONS = """
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT,
    password TEXT,
    email TEXT,
    isAdmin BOOLEAN,
    isBanned BOOLEAN
)
"""

INSERT_PERSON_QUERY = """
INSERT INTO persons (login, password, email, isAdmin, isBanned)
VALUES (?, ?, ?, false, false)
"""

INSERT_ADMIN = """
INSERT INTO persons (login, password, email, isAdmin, isBanned)
VALUES ('GoSum216', 'qwerty', 'qwerty@qwerty', true, false)
"""

DELETE_PERSON = """DELETE FROM persons WHERE is = ?"""

BAN_PERSON = """UPDATE persons SET isBanned = true WHERE id = ?"""

ADMIN_PERSON = """UPDATE persons SET isAdmin = true WHERE id = ?"""


################################################################

CREATE_TABLE_COMMENTS = """
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idPerson INTEGER,
    idPost INTEGER,
    time DATETIME DEFAULT CURRENT_TIMESTAMP,
    text TEXT,
    FOREIGN KEY (idPerson) REFERENCES persons (id), 
    FOREIGN KEY (idPost) REFERENCES posts (id)
)
"""
