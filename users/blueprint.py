from flask import Blueprint, render_template, redirect, request, flash
from flask.globals import session
from flask.helpers import url_for
from config import db
from werkzeug.security import generate_password_hash, check_password_hash

users = Blueprint('users', __name__, template_folder='templates', static_folder='static')

@users.route('/', methods=['POST', 'GET'])
def index():
    if 'userLogged' in session:
        return redirect(url_for('main'))
    return render_template('users/index.html')

@users.route('/log_in', methods=['POST', 'GET'])
def log_in():
    if 'userLogged' in session:
        return redirect(url_for('main'))
    elif request.method == 'POST':
        if request.form['login'] == '123' and request.form['password'] == '123':
            session['userLogged'] = request.form['login']
            return redirect(url_for('main'))
        else:
            flash('Неправильно введен логин или пароль', category="log_in")
    return redirect(url_for('users.index'))

@users.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        if len(request.form['login']) > 4 and len(request.form['password']) > 4 and len(request.form['email']) > 4 and request.form['password'] == request.form['password2']:
            hash = generate_password_hash(request.form['password'])
            res = db.insert_user(request.form['login'], hash, request.form['email'])
            if res:
                return redirect(url_for('main'))
            else:
                redirect(url_for('users.index'))
        else:
            flash('Неправильно заполнены поля', category="registration")
    return redirect(url_for('users.index'))

@users.route('/log_out')
def log_out():
    if 'userLogged' in session:
        session.pop('userLogged', None)
    return redirect(url_for('index'))
    