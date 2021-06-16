from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/user_verification')
def user_verification():
    return render_template('user_verification.html')