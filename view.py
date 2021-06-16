from app import app, db
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    posts = db.get_posts()
    posts = [dict(post) for post in posts]
    return render_template('index.html', posts=posts)

@app.route('/user_verification')
def user_verification():
    return render_template('user_verification.html')