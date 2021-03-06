import sqlite3
import os
from flask import Flask, render_template, request, g, flash, abort
from FDataBase import FDataBase

# конфигурация
DATABASE = '/tmp/flsuite.db'
DEBUG = True
SECRET_KEY = 'j3g1j2h41j4124'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsuite.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row # запись не в картеже, а в словаре
    return conn


def get_db(): # соединение с бд, если оно ещё не установлено
    if not hasattr(g, 'link_db'): # если есть св-во link_db - значит соединение уже есть
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu=dbase.getMenu())

@app.teardown_appcontext
def close_db(error):
    # закрываем соединение с бд если оно было установлено
    if hasattr(g, 'link_db'):
        g.link_db.close()

def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


if __name__ == "__main__":
    app.run(debug=True)
