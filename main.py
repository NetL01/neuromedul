from flask import Flask, render_template, url_for, request, flash, session, redirect, abort

app = Flask(__name__)
app.config["SECRET_KEY"] = 'j3g1j2h41j4124'
menu = ["Установка", "Приложение", "Обратная связь"]

@app.route("/title/<title>")
@app.route("/")
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)

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

@app.route("/login", methods=["POST", "GET"])
def login():
    if "userLogged" in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == "POST" and request.form['username'] == "selfedu" and request.form["psw"] == "123":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title='Авторизация', menu=menu)

@app.errorhandler(404)
def pagenotfound(error):
    return url_for('index')
@app.route("/about")
def about():
    print( url_for(about))
    return render_template('base.html', menu=menu, title='NetL01')

if __name__ == "__main__":
    app.run(debug=True)
