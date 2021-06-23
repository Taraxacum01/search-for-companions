from db.query import * 
import os.path
import sqlite3

class Database:
    
    def __init__(self, database_name):
        self.database_name = database_name

    def len_list(conn):
        cursor = conn.cursor()
        cursor.execute("select * from posts")
        results = cursor.fetchall()
        return 2 + len(results)

    def get_db_connection(self):
        conn = sqlite3.connect(self.database_name)
        conn.row_factory = sqlite3.Row
        return conn

    def create_db(self):
        with self.get_db_connection() as conn:
            conn.execute(CREATE_TABLE_POSTS)
            conn.execute(CREATE_TABLE_PERSONS)
            conn.execute(CREATE_TABLE_COMMENTS)

    def init_db(self):
        if not os.path.exists(self.database_name):
            self.create_db()
            with self.get_db_connection() as conn:
                conn.execute(INSERT_QUERY)
                conn.commit()

    def get_posts(self):
        with self.get_db_connection() as conn:
            posts = conn.execute(POSTS_QUERY).fetchall()
        return posts

    def get_driver_posts(self):
        with self.get_db_connection() as conn:
            posts = conn.execute(POSTS_DRIVER_QUERY).fetchall()
        return posts

    def get_passengers_posts(self):
        with self.get_db_connection() as conn:
            posts = conn.execute(POSTS_PASSENGERS_QUERY).fetchall()
        return posts

    def get_post(self, id):
        with self.get_db_connection() as conn:
            post = conn.execute(POST_QUERY, [id]).fetchone()
        return post

    def insert_post(self, post):
        with self.get_db_connection() as conn:
            parameters = [post['isDriver'], post['isType'], post['idPerson'], post['idBeginPoint'], post['idEndPoint'], post['text'], post['time'], post['driverName']]
            cur = conn.cursor()
            cur.execute(INSERT_POST_QUERY, parameters)
            conn.commit()
        return True

    def delete_post(self, id):
        with self.get_db_connection() as conn:
            conn.execute(DELETE_POST, [id])
            conn.commit()
        return 

    def insert_user(self, login, password, email):
        with self.get_db_connection() as conn:
            cur = conn.cursor()
            cur.execute(f"SELECT COUNT() as 'count' FROM persons WHERE email LIKE '{email}'")
            res = cur.fetchone()
            cur.execute(f"SELECT COUNT() as 'count' FROM persons WHERE login LIKE '{login}'")
            result = cur.fetchone()

            if res['count'] > 0 or result['count'] > 0:
                return False
            parameters = [login, password, email]
            cur.execute(INSERT_PERSON_QUERY, parameters)
            conn.commit()
        return True

    def get_user(self, user_id):
        with self.get_db_connection() as conn:
            person = conn.execute(PERSON_QUERY, [user_id]).fetchone()
        return person

    def get_user_by_login(self, login):
        with self.get_db_connection() as conn:
            person = conn.execute(PERSON_BY_LOGIN_QUERY, [login]).fetchone()
            if not person:
                return False
            return person

    def insert_comment(self, idPerson, idPost, text):
        with self.get_db_connection() as conn:
            parameters = [idPerson, idPost, text]
            cur = conn.cursor()
            cur.execute(INSERT_COMMENT, parameters)
            conn.commit()
        return True


    def get_comments(self, idPost):
        with self.get_db_connection() as conn:
            comments = conn.execute(GET_COMMENTS_BY_ID_POST, [idPost]).fetchall()
        return comments

    def check_id(self, id):
        try:
            print(*self.get_post(id))
        except:
            return False
        return True
        