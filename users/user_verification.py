from flask import request
# from app.db.database import Database

DATABASE = 'posts.db'

# db = Database(DATABASE)
# db.init_db()

class User():
    def __init__(self, id, name, username, password, login, email):
        self.name = name
        self.username = username
        self.password = password
        self.login = login
        self.email = email
        self.is_admin = 0
        self.id = id

def check_user():
    
    return False

def add_user():
    # if request.form:
    #     username = request.form.get('username')
    #     login = request.form.get('login')
    #     password = request.form.get('password')
    #     email = request.form.get('email')
    #     post = {'username': username, 'login': login, 'password': password, 'email': email}
    #     db.insert_post(post)
    return