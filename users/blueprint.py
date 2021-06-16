from flask import Blueprint, render_template, redirect
from users.user_verification import check_user, add_user

users = Blueprint('users', __name__, template_folder='templates', static_folder='static')

@users.route('/')
def index():
    return render_template('users/index.html')

@users.route('/log_in', methods=['post'])
def log_in():
    
    return redirect('/main')
    
@users.route('/registration', methods=['post'])
def registration():
    if(not check_user()):
        add_user()
    return redirect('/main')