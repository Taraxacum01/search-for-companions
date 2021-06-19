from app import app
from config import db
from flask import render_template, redirect
from flask.globals import session
from flask.helpers import url_for

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    if 'userLogged' in session:
        return render_template('main.html', posts=db.get_posts())
    return redirect(url_for('index'))

@app.route('/posts/<int:id>')
def about(id):
    if 'userLogged' in session:
        if id not in range(1, len(db.get_posts()) + 1):
            return "", 404
        return render_template('post.html', post=db.get_post(id))
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html')

@app.route('/addpost')
def addpost():
    return render_template('addpost.html')