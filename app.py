from flask import Flask
from config import Configuration
from db.database import Database

DATABASE = 'posts.db'

db = Database(DATABASE)
db.init_db()

app = Flask(__name__)
app.config.from_object(Configuration)