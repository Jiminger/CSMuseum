import serial
import mysql.connector
from threading import Thread

# TODO: Serial connections for other two cases

# Case 3 Serial Connection
ser3 = serial.Serial('/dev/tty.usbmodem14101', 9600, timeout=1)
ser3.reset_input_buffer()


def turn_on_case(case_number):
    indices = get_item_indexes(case_number, 1)
    if case_number == "case_one":
        pass
    elif case_number == "case_two":
        pass
    elif case_number == "case_three":
        ser3.write(bytes(str(indices[1]), 'utf-8'))
        ser3.write(bytes(str(indices[2]), 'utf-8'))


def turn_off_case(case_number):
    if case_number == "case_one":
        pass
    elif case_number == "case_two":
        pass
    elif case_number == "case_three":
        ser3.write(bytes('-1', 'utf-8'))
        ser3.write(bytes('-1', 'utf-8'))


def light_entire_museum():
    thread_one = Thread(target=turn_on_case("case_one"))
    thread_two = Thread(target=turn_on_case("case_two"))
    thread_three = Thread(target=turn_on_case("case_three"))

    thread_one.start()
    thread_two.start()
    thread_three.start()

    thread_one.join()
    thread_two.join()
    thread_three.join()


def light_specific_case(case_number):
    if case_number == "case_one":
        pass
    elif case_number == "case_two":
        pass
    elif case_number == "case_three":
        turn_off_case("case_one")
        turn_off_case("case_two")
        turn_on_case("case_three")


def light_specific_item(case_number, item_id):
    indices = get_item_indexes(case_number, item_id)
    if case_number == "case_one":
        pass
    elif case_number == "case_two":
        pass
    elif case_number == "case_three":
        turn_off_case("case_one")
        turn_off_case("case_two")
        ser3.write(bytes(str(indices[1]), 'utf-8'))
        ser3.write(bytes(str(indices[2]), 'utf-8'))


def get_item_indexes(case_number, item_id):
    my_db = mysql.connector.connect(
        host="localhost",
        user="",
        password="",
        database="CSMuseum"
    )

    my_cursor = my_db.cursor()

    my_cursor.execute("SELECT start_index, end_index FROM " + case_number + " WHERE item_id =" + item_id)

    my_result = my_cursor.fetchall()

    my_cursor.close()
    my_db.close()

    return case_number, my_result[0], my_result[1]

