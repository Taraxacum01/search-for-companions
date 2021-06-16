from app import app, db
from flask import render_template, redirect

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    posts = db.get_posts()
    posts = [dict(post) for post in posts]
    return render_template('main.html', posts=posts)