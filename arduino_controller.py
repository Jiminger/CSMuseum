import serial
import db_controller as db
from threading import Thread

# TODO: Serial connections for other two cases

# Case 3 Serial Connection
ser3 = serial.Serial('/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_75135303739351508042-if00', 115200,
                     timeout=1)
ser3.reset_input_buffer()


# Method used to format the indexes to be messaged to the arduino
def format_input(start_index, end_index):
    return '<' + str(start_index) + ',' + str(end_index) + '>'


def turn_on_case(case_id):
    indices = db.get_item_indexes(case_id, 0)
    if case_id == 1:
        pass
    elif case_id == 2:
        pass
    elif case_id == 3:
        ser3.write(indices.encode())


def turn_off_case(case_id):
    if case_id == 1:
        pass
    elif case_id == 2:
        pass
    elif case_id == 3:
        ser3.write('<-1,-1>'.encode())


def light_entire_museum():
    # thread_one = Thread(target=turn_on_case("case_one"))
    # thread_two = Thread(target=turn_on_case("case_two"))
    thread_three = Thread(target=turn_on_case(3))

    # thread_one.start()
    # thread_two.start()
    thread_three.start()

    # thread_one.join()
    # thread_two.join()
    thread_three.join()


def light_specific_case(case_id):
    if case_id == 1:
        pass
    elif case_id == 2:
        pass
    elif case_id == 3:
        #   turn_off_case(1)
        #   turn_off_case(2)
        turn_on_case(3)


def light_specific_item(case_id, item_id):
    indices = db.get_item_indexes(case_id, item_id)
    if case_id == "1":
        pass
    elif case_id == "2":
        pass
    elif case_id == "3":
        #  turn_off_case("case_one")
        # turn_off_case("case_two")
        #  ser3.write(bytes(str(indices[1]), 'utf-8'))
        # ser3.write(bytes(str(indices[2]), 'utf-8'))
        ser3.write(indices.encode())


"""
def get_item_indexes(case_id, item_id):
    my_db = mysql.connector.connect(
        host="localhost",
        user='',
        password='',
        database="CSMuseum"
    )

    my_cursor = my_db.cursor()

    my_cursor.execute("SELECT start_index, end_index FROM " + case_id + " WHERE item_id =" + str(item_id))

    my_result = my_cursor.fetchall()

    my_cursor.close()
    my_db.close()

    return case_id, format_input(str(my_result[0][0]), str(my_result[0][1]))
"""
