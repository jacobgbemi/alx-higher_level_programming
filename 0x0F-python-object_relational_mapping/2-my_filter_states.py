#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # create cursor to exec queries using SQL; match arg given
    cursor = db.cursor()
    sql_cmd = "SELECT * \
                 FROM states \
                 WHERE name LIKE '{:s}' ORDER BY id ASC".format(argv[4])
    cursor.execute(sql_cmd)
    for state in cursor.fetchall():
        if state[1] == argv[4]:
            print(state)
    cursor.close()
    db.close()
