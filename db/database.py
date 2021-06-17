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
                conn.execute(INSERT_QUERY)
                conn.execute(INSERT_QUERY)
                conn.execute(INSERT_QUERY)
                posts = conn.execute(DELETE_POST, [2])
                n = Database.len_list(conn)
                for i in range(3, n):
                    conn.execute(CHANGE_POST_ID, [i])
                conn.execute(INSERT_ADMIN)
                conn.commit()

    def get_posts(self):
        with self.get_db_connection() as conn:
            posts = conn.execute(POSTS_QUERY).fetchall()
        return posts

    def get_post(self, id):
        with self.get_db_connection() as conn:
            post = conn.execute(POST_QUERY, [id]).fetchone()
        return post

    def insert_post(self, post):
        with self.get_db_connection() as conn:
            parameters = [post['isDriver'], post['idPerson'], post['idBeginPoint'], post['idEndPoint'], post['text']]
            cur = conn.cursor()
            cur.execute(INSERT_POST_QUERY, parameters)
            lastrowid = cur.lastrowid
            conn.commit()
        return lastrowid

    def delete_post(self, id):
        with self.get_db_connection() as conn:
            posts = conn.execute(DELETE_POST, [id])
            n = Database.len_list(conn)
            for i in range(id+1, n):
                posts = conn.execute(CHANGE_POST_ID, [i])
            conn.commit()
        return posts 

    def insert_user(self, login, password, email):
        with self.get_db_connection() as conn:
            parameters = [login, password, email]
            cur = conn.cursor()
            cur.execute(INSERT_PERSON_QUERY, parameters)
            conn.commit()
        return True

    # def insert_tag(self, tag):
    #     with self.get_db_connection() as conn:
    #         parameters = [tag]
    #         cur = conn.cursor()
    #         tag = cur.execute('SELECT * FROM tags WHERE title = ?', parameters).fetchone()
    #         if tag:
    #             lastrowid = tag['id']            
    #         else:
    #             cur.execute(INSERT_TAG_QUERY, parameters)
    #             lastrowid = cur.lastrowid
    #             conn.commit()
    #     return lastrowid

    # def insert_post_tag(self, post_id, tag_id):
    #     with self.get_db_connection() as conn:
    #         parameters = [post_id, tag_id]
    #         conn.execute(INSERT_POST_TAG_QUERY, parameters)
    #         conn.commit()

    # def get_max_id(self, table):
    #     with self.get_db_connection() as conn:
    #         max_id = conn.execute(f"SELECT MAX(id) as id FROM {table}").fetchone()
    #     return max_id["id"]

    # def select_tags_for_post(self, post_id):
    #     with self.get_db_connection() as conn:
    #         parameters = [post_id]
    #         tags = conn.execute(TAGS_FOR_POST, parameters).fetchall()
    #     tags = [dict(tag) for tag in tags]
    #     return tags

    # def select_count_for_tags(self):
    #     with self.get_db_connection() as conn:
    #         tags = conn.execute(SELECT_COUNT_POSTS_FOR_TAGS).fetchall()
    #     tags = [dict(tag) for tag in tags]
    #     return tags