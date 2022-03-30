from flask import Flask
from flask import render_template

#import arduino_controller as controller

app = Flask(__name__)


# Index Page
@app.route('/')
def index():
    controller.light_entire_museum()
    return render_template("index.html")


# Case One Pages
@app.route('/case_1/')
def case_1():
    controller.turn_on_case(1)
    return render_template("case_1.html")

@app.route('/case_1/<id>')
def get_item(id):
    return id

# Case Two Pages
@app.route('/case_2/')
def case_2():
    controller.turn_on_case(2)
    return render_template("case_2.html")

@app.route('/case_2/<id>')
def get_item(id):
    return id


# Case Three Pages
@app.route('/case_3/')
def case_3():
    controller.turn_on_case(3)
    return render_template("case_3.html")

@app.route('/case_3/<id>')
def get_item(id):
    return id



if __name__ == "__main__":
    app.run()