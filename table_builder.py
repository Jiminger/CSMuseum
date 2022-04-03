"""Module Used to Build Database Item Table From Text File."""

import mysql.connector
import info

f = open("Museum Items.txt", "r")

my_db = mysql.connector.connect(
    host="localhost",
    user=info.get_db_user(),
    password=info.get_db_pass(),
    database="CSMuseum"
)

my_cursor = my_db.cursor()


def insert_into_table(values):
    case_id = values[0]
    item_id = values[1]
    item_name = values[2]
    item_desc = values[3]
    img_path = values[4]
    start_index = values[5]
    end_index = values[6]

    sql_insert = "INSERT INTO customers (case_id, item_id, item_name, item_desc, img_path, start_index, end_index) " \
                 "VALUES {},{},{},{},{},{},{}".format(case_id, item_id, item_name, item_desc, img_path, start_index,
                                                      end_index)
    my_cursor.execute(sql_insert)
    my_db.commit()


for x in f:
    if x[0] != '#' and x != '\n':
        insert_into_table(x.strip('\n').split(','))
