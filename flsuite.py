import sqlite3
import os
from flask import Flask, render_template, request

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

# if __name__ == "__main__"
#    app.run(debug=True)
