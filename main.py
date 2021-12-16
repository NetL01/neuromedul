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

@app.route('/tool', methods=['POST', 'GET'])
def tool():
    try:
        if "userLogged" not in session:
            return render_template('someerror.html')
        # print('video settings: ', request.form['inlineRadioOptions'])
        # print('tools: ', request.form())
        # print('Datasets: ', request.form())
        elif request.method == "POST":
            option = request.form
            print(option)
            print(request.form['inlineRadioOptions1'])
            if request.form['inlineRadioOptions1'] == 'Canvas':
                return canvas()
            elif request.form['inlineRadioOptions1'] == 'Text editor':
                return text_editor()
            elif request.form['inlineRadioOptions1'] == 'Dictaphone':
                return dictaphone()
            try:
                print(request.form['inlineRadioOptions2'])
                if request.form['inlineRadioOptions2'] == 'Accelerometer':
                    return accelerometer()
                if request.form['inlineRadioOptions1'] == 'Gyroscope':
                    return gyro()
                if request.form['inlineRadioOptions1'] == 'Clock':
                    return clock()
                if request.form['inlineRadioOptions1'] == 'Compass':
                    return compass()
            except:
                res = 1
        return render_template('tool.html')
    except:
        return render_template('someerror.html')

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


def canvas():
    code = [
            'import requests'
            'from kivy.clock import Clock',
             'from kivy.lang import Builder',
             'from kivy.app import App',
             'from kivy.uix.widget import Widget',
             'from kivy.graphics import (Color, Ellipse, Rectangle, Line)',
             'from kivy.uix.button import Button',
             'from kivy.core.window import Window',
             'from random import random',
             'from kivy.uix.pagelayout import PageLayout',
             '',
             '',
             'class PainterWidget(Widget):',
             '  def on_touch_down(self, touch):',
             '       with self.canvas:',
             '            Color(1., 0, 0, 0.49)',
             '           rad = 10',
             '           Ellipse(pos = (touch.x - rad/2, touch.y - rad/2), size= (rad, rad))',
             "            touch.ud['line'] = Line(points = (touch.x, touch.y), width = 10)",
             '',
             "",
             '    def on_touch_move(self, touch):',
             "        touch.ud['line'].points += (touch.x, touch.y)",
            'class PaintApp(App):',
            '    def build(self):',
            '        parent = Widget()',
            '        self.painter = PainterWidget()',
            '        parent.add_widget(self.painter)',
            '        Clock.schedule_once(self.set_background, 0)',
            '',
            "",
            '       # parent.add_widget(Button(text="Назад", on_press=self.save_canvas, size=(100, 50)))',
            '       parent.add_widget(Button(text="Очистить", on_press=self.clear_canvas, size=(100, 50), pos = (100, 0)))',
            '       parent.add_widget(Button(text="Отправить", on_press=self.screen_canvas, size=(100, 50), pos=(200, 0)))',
            '       return parent',
            "",
            "",
            '    def clear_canvas(self, instance):',
            '        self.painter.canvas.clear()',
            '',
            "",
            '    def save_canvas(self, instance):',
            '        self.painter.size = (Window.size[0], Window.size[1])',
            "        self.painter.export_to_png('image.png')",
            "",
            "",
            '    def screen_canvas(self, instance):',
            "        scr = Window.screenshot('screem.png')",
            "        url = 'http://file.api.wechat.com/cgi-bin/media/upload?access_token=ACCESS_TOKEN&type=TYPE'",
            "        files = {'media': open('test.jpg', 'rb')}",
            "        requests.post(url, files=files)'",
            '',
            '',
            '    def set_background(self, *args):',
            '        self.root_window.bind(size=self.do_resize)',
            '        with self.root_window.canvas.before:',
            "            self.bg = Rectangle(source='map.png', pos=(0, 0), size=(self.root_window.size))",
            '',
            '    def do_resize(self, *args):',
            '        self.bg.size = self.root_window.size',
            "",
            'if __name__ == "__main__":',
            '    PaintApp().run()']
    return render_template('getcode.html', code=code)




def text_editor():
    pass

def dictaphone():
    pass

def accelerometer():
    pass

def gyro():
    pass

def clock():
    pass

def compass():
    pass




@app.route("/about")
def about():
    print( url_for(about))
    return render_template('base.html', title='NetL01')

if __name__ == "__main__":
    app.run(debug=True)
