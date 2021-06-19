from datetime import datetime
from flask import Flask
from config import Configuration
from users.blueprint import users
import datetime

app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(users, url_prefix="/user_verification")

app.permanent_session_lifetime = datetime.timedelta(days=10)