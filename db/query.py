CREATE_TABLE_POSTS = """
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    isDriver BOOLEAN,
    isType TEXT,
    idPerson INTEGER,
    idBeginPoint TEXT,
    idEndPoint TEXT,
    time DATETIME DEFAULT CURRENT_TIMESTAMP,
    text TEXT,
    driverName TEXT,
    FOREIGN KEY (idPerson) REFERENCES persons (id) 
     
);
"""

POSTS_QUERY = """SELECT * FROM posts"""
POST_QUERY = """SELECT * FROM posts WHERE id = ?"""

INSERT_POST_QUERY = """
INSERT INTO posts (isDriver, isType, idPerson, idBeginPoint, idEndPoint, text, time, driverName)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

DELETE_POST = """DELETE FROM posts WHERE id = ?"""

CHANGE_POST_ID = """UPDATE posts SET id = id-1 WHERE id = ?"""

COUNT_POST = """SELECT COUNT(*) FROM posts"""

INSERT_QUERY = """
INSERT INTO posts (isDriver, isType, idPerson, idBeginPoint, idEndPoint, text, time, driverName)
VALUES (true, 'driver', 1, 'Вертодром', 'ЖД вокзал', 'Я из будущего, я вас жду', '20.06.2021 | 21:00', '12345')
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

PERSON_QUERY = """SELECT * FROM persons WHERE id = ?"""

PERSON_BY_LOGIN_QUERY = """SELECT * FROM persons WHERE login = ? LIMIT 1"""

INSERT_ADMIN = """
INSERT INTO persons (login, password, email, isAdmin, isBanned)
VALUES ('GoSum216', 'qwerty', 'qwerty@qwerty', true, false)
"""

DELETE_PERSON = """DELETE FROM persons WHERE is = ?"""

CHANGE_PERSON_ID = """UPDATE persons SET id = id-1 WHERE id = ?"""

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

INSERT_COMMENT = """
INSERT INTO comments (idPerson, idPost, text)
VALUE (?, ?, ?)
"""

GET_COMMENTS_BY_ID_POST = """SELECT * FROM comments WHERE idPost = ? ORDER BY time DESC"""