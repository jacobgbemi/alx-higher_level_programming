#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
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
    sql_cmd = "SELECT cities.name \
                 FROM states \
                 INNER JOIN cities ON states.id = cities.state_id \
                 WHERE states.name LIKE %s \
                 ORDER BY cities.id ASC"""
    cursor.execute(sql_cmd, (argv[4], ))

    # format the printing of cities of same state separated by commas
    print(', '.join(["{:s}".format(city[0]) for city in cursor.fetchall()]))

    cursor.close()
    db.close()
