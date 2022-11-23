#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
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

    # create cursor to exec queries using SQL; join two tables for all info
    cursor = db.cursor()
    sql_cmd = "SELECT cities.id, cities.name, states.name \
                 FROM states \
                 INNER JOIN cities ON states.id = cities.state_id \
                 ORDER BY cities.id ASC"
    cursor.execute(sql_cmd)

    for city in cursor.fetchall():
        print(city)
    cursor.close()
    db.close()
