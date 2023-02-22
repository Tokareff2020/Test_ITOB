from flask import Flask, request, render_template, jsonify, redirect

from teapot.const import BOILING_TIME
from teapot.teapot import Teapot

app = Flask(__name__)
teapot = Teapot()


@app.route('/')
def home():
    """Главная страница, в которой содержаться функции взаимодействия с чайником"""

    return render_template('home.html')


@app.route('/teapot/turn_on', methods=['GET', 'POST'])
def teapot_turn_on():
    if not teapot.water_amount:
        return redirect('http://127.0.0.1:5000/teapot/pour_water')
    teapot.turn_on()
    return render_template('finish.html', teapot=teapot)


@app.route('/teapot/pour_water', methods=['GET', 'POST'])
def teapot_pour_water():
    if request.form.get('water_amount'):
        water_amount = request.form.get('water_amount')
        teapot.pour_water(water_amount)

    return render_template('pour_water.html', water_amount=teapot.water_amount)


@app.route('/teapot/turn_off', methods=['GET', 'DELETE'])
def teapot_turn_off():
    if not teapot.water_amount:
        return redirect('http://127.0.0.1:5000/teapot/pour_water')
    print(teapot.turn_off())
    return render_template('stop.html', teapot=teapot)


if __name__ == '__main__':
    app.run()
