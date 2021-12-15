from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, send_from_directory

app = Flask(__name__)
app.config["SECRET_KEY"] = 'j3g1j2h41j4124'


def get_db(): # соединение с бд, если оно ещё не установлено
    pass
#    if not hasattr(g, 'link_db'): # если есть св-во link_db - значит соединение уже есть
#        g.link_db = connect_db()
#    return g.link_db

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/tool')
def tool():
    pass

@app.route('/account/<username>')
def account(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        return render_template("someerror.html")
    return render_template('account.html', title=username)


@app.route('/signout')
def signout():
    session.clear()
    print('Сессия пользователя завершена')
    return render_template('signout.html')


@app.route('/mainpage')
def mainpage():
    return render_template('mainpage.html')


@app.route("/signin", methods=["POST", "GET"])
def signin():
    if "userLogged" in session:
        print('Пользователь уже в сессии')
        return redirect(url_for('account', username=session['userLogged']))
    elif request.method == "POST" and request.form['username'] == "rkraud@bk.ru" and request.form["psw"] == "102312203":
        session['userLogged'] = request.form['username']
        print('Пользователь добавлен в сессию')
        return redirect(url_for('account', username=session['userLogged']))
    return render_template('signin.html', title='Авторизация')


@app.errorhandler(404)
def pagenotfound(error):
    return render_template('errorhandler.html')







@app.route("/")
def index():
    db = get_db()
    return render_template('index.html', menu=[])


@app.route('/profile/<username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f"Профиль пользователя: {username}"

@app.route("/contact", methods=["POST", "GET"])
def contact():

    if request.method == 'POST':
        print(request.form['username'])
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')
    return render_template("contact.html")





@app.route("/about")
def about():
    print( url_for(about))
    return render_template('base.html', menu=menu, title='NetL01')

if __name__ == "__main__":
    app.run(debug=True)
