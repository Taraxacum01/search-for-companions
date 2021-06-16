from flask import Flask
from config import Configuration
from db.database import Database
from users.blueprint import users

DATABASE = 'posts.db'

db = Database(DATABASE)
db.init_db()

app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(users, url_prefix="/user_verification")