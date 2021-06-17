from flask import Blueprint, render_template, redirect, request, flash
from flask.globals import session
from flask.helpers import url_for
from config import db

users = Blueprint('users', __name__, template_folder='templates', static_folder='static')

@users.route('/', methods=['POST', 'GET'])
def index():
    # session.pop('userLogged', None)
    if 'userLogged' in session:
        return redirect(url_for('main'))
    elif request.method == 'POST':
        if request.form['login'] == '123' and request.form['password'] == '123':
            session['userLogged'] = request.form['login']
            return redirect(url_for('main'))
        else:
            flash('Неправильно введен логин или пароль')
        # login = request.form.get('login')
        # username = login
        # password = request.form.get('password')
        # email = request.form.get('email')
        # post = {'username': username, 'login': login, 'password': password, 'email': email}
        # db.insert_post(post)

    return render_template('users/index.html')