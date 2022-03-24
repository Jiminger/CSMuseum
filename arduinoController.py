import serial
import mysql.connector
from threading import Thread

# TODO: Serial connections for other two cases

# Case 3 Serial Connection
ser3 = serial.Serial('/dev/tty.usbmodem14101', 9600, timeout=1)
ser3.reset_input_buffer()


def light_entire_museum():
    def light_cases(case_number):
        if case_number == "case_one":
            pass
        elif case_number == "case_two":
            pass
        elif case_number == "case_three":
            indices = get_item_indexes("case_three", 1)
            ser3.write(bytes(str(indices[0]), 'utf-8'))
            ser3.write(bytes(str(indices[1]), 'utf-8'))

    thread_one = Thread(target=light_cases("case_one"))
    thread_two = Thread(target=light_cases("case_two"))
    thread_three = Thread(target=light_cases("case_three"))

    thread_one.start()
    thread_two.start()
    thread_three.start()

    thread_one.join()
    thread_two.join()
    thread_three.join()


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


"""
def lightController():
    user = input("Enter input: ")
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
