from app import app, db
from flask import render_template, redirect
from users.user_verification import check_user, add_user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    posts = db.get_posts()
    posts = [dict(post) for post in posts]
    return render_template('main.html', posts=posts)

@app.route('/user_verification')
def user_verification():
    return render_template('user_verification.html')

@app.route('/log_in', methods=['post'])
def log_in():
    
    return redirect('/main')
    

@app.route('/registration', methods=['post'])
def registration():
    if(not check_user()):
        add_user()
    return redirect('/main')