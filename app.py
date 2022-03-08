from flask import Flask
from flask import render_template

import serial

app = Flask(__name__)
ser = serial.Serial('/dev/tty.usbmodem14101', 9600, timeout=1)
ser.reset_input_buffer()


def lightController(user):
    if user == '1':
        x = '0'
        y = '60'
        ser.write(bytes(x, 'utf-8'))
        ser.write(bytes(y, 'utf-8'))
    elif user == '2':
        x = '5'
        y = '10'
        ser.write(bytes(x, 'utf-8'))
        ser.write(bytes(y, 'utf-8'))
    elif user == '0':
        x = '0'
        y = '20'
        ser.write(bytes(x, 'utf-8'))
        ser.write(bytes(y, 'utf-8'))


@app.route('/')
@app.route('/home')
def hello():
    lightController("1")
    return render_template("index.html")


@app.route('/2')
def hello2():
    lightController("2")
    return 'item 2'

@app.route('/0')
def hello3():
    lightController("0")
    return 'item 3'
