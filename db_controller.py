import mysql.connector
import info


def open_connection():
    my_db = mysql.connector.connect(
        host="localhost",
        user=info.get_db_user(),
        password=info.get_db_pass(),
        database="CSMuseum"
    )

    my_cursor = my_db.cursor()

    return my_db, my_cursor


def close_connection(connection):
    for c in connection:
        c.close()


def format_input(start_index, end_index):
    return '<' + str(start_index) + ',' + str(end_index) + '>'


def get_item_indexes(case_id, item_id):
    connection = open_connection()
    my_cursor = connection[1]
    my_cursor.execute("SELECT start_index, end_index FROM Items WHERE case_id= " + str(case_id) +
                      " AND item_id =" + str(item_id) + ";")

    my_result = my_cursor.fetchall()

    close_connection(connection)
    return format_input(str(my_result[0][0]), str(my_result[0][1]))


def get_item_information(case_id, item_id):
    connection = open_connection()
    my_cursor = connection[1]
    my_cursor.execute("SELECT item_name, item_desc, img_path FROM Items WHERE case_id =" + str(case_id) +
                      " AND  item_id =" + str(item_id) + ";")

    my_result = my_cursor.fetchall()
    close_connection(connection)

    return my_result
