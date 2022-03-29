from flask import Flask
from flask import render_template

import serial
import arduino_controller as controller

app = Flask(__name__)

# Commented out for testing of the arduinoController class
# ser = serial.Serial('/dev/tty.usbmodem14101', 9600, timeout=1)
# ser.reset_input_buffer()

"""
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
"""


@app.route('/')
def index():
    controller.light_entire_museum()
    return render_template("index.html")


# TODO : route to other web pages
"""
@app.route('/case_one')
def case1():
    lightController("2")
    return 'case_1'


@app.route('/case_two')
def case2():
    lightController("0")
    return 'case_two'


@app.route('/case_three')
def case2():
    lightController("0")
    return 'case_3'
"""
