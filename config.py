from db.database import Database
class Configuration(object):
    DEBUG = True
    SECRET_KEY = 'jhf8yr2^&(JO90#UOJdsf<,3fl#'

DATABASE = 'posts.db'
db = Database(DATABASE)
db.init_db()
