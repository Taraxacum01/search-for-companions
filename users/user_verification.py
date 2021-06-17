from flask import request
from db.database import Database
from config import db

class User():
    def __init__(self, id, username, password, login, email):
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
    #     login = request.form.get('login')
    #     username = login
    #     password = request.form.get('password')
    #     email = request.form.get('email')
    #     post = {'username': username, 'login': login, 'password': password, 'email': email}
    #     db.insert_post(post)
    return
