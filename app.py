from flask import Flask
from flask import render_template

# import arduino_controller
# import db_controller

app = Flask(__name__)


# Index Page
@app.route('/')
def index():
    # controller.light_entire_museum()
    return render_template("index.html")


# Case One Pages
@app.route('/case_1/')
def case_1():
    # controller.turn_on_case(1)
    return render_template("case_1.html")


# Case Two Pages
@app.route('/case_2/')
def case_2():
    # controller.turn_on_case(2)
    return render_template("case_2.html")


# Case Three Pages
@app.route('/case_3/')
def case_3():
    # controller.turn_on_case(3)
    return render_template("case_3.html")


@app.route('/case_<case_id>/item_<item_id>')
def item_page(case_id, item_id):
    item_info = db_controller.get_item_information(case_id,item_id)
    return render_template("item.html", item_name=item_info[0], item_desc=item_info[1], img_path=item_info[2])


if __name__ == "__main__":
    app.run()
