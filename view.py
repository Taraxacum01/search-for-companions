from app import app
from config import db
from flask import render_template, redirect

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html', posts=db.get_posts())

@app.route('/posts/<int:id>')
def about(id):
    if id not in range(1, len(db.get_posts()) + 1):
        return "", 404
    return render_template('post.html', post=db.get_post(id))
    
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html')