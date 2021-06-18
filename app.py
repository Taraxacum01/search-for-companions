from flask import Flask
from config import Configuration
from users.blueprint import users

app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(users, url_prefix="/user_verification")
