from app import app
from config import db
from flask import render_template, redirect, request
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

@app.route('/drivers')
def drivers():
    if 'userLogged' in session:
        return render_template('main.html', posts=db.get_driver_posts())
    return redirect(url_for('index'))

@app.route('/passengers')
def passengers():
    if 'userLogged' in session:
        return render_template('main.html', posts=db.get_passengers_posts())
    return redirect(url_for('index'))

@app.route('/posts/<int:id>')
def about(id):
    if 'userLogged' in session:
        if db.check_id(id):
            return render_template('post.html', post=db.get_post(id))
        return render_template('page404.html')
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html')

@app.route('/addpost', methods=['POST', 'GET'])
def addpost():
    if request.method == 'POST':
        select = request.form.getlist('select')
        print(select)
        if select[0] == 'driver':
            isDriver = True
            is_type = 'driver'
        if select[0] == 'passenger':
            isDriver = False
            is_type = 'passenger'
        id_person = session['userLoggedID']
        begin = request.form.get('BeginPoint')
        end = request.form.get('EndPoint')
        text = request.form.get('message')
        time = request.form.get('date') + ' | ' + request.form.get('time')
        name = session['userLogged']

        post = {'isDriver': isDriver, 'isType': is_type, 'idPerson': id_person, 'idBeginPoint': begin, 'idEndPoint': end, 'text': text, 'time': time, 'driverName': name}
        res = db.insert_post(post)
        if res:
            return redirect(url_for('main'))
    return render_template('addpost.html')

@app.route('/delete_post/<int:id><name>')
def delete_post(id, name):
    if 'userLogged' in session:
        if session['userLogged'] == name or session['userLoggedisAdmin']:
            db.delete_post(id)
        return redirect(url_for('main'))
    return redirect(url_for('index'))