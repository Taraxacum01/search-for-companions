from db.database import Database
class Configuration(object):
    DEBUG = True

DATABASE = 'posts.db'
db = Database(DATABASE)
db.init_db()
