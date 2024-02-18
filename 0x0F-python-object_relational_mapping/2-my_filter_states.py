#!/usr/bin/python3
""" script lists all states from the database hbtn_0e_0_usa """

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1], port=3306,
                         db=sys.argv[3], passwd=sys.argv[2])

    curserr = db.cursor()
    curserr.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
        ORDER BY id ASC".format(sys.argv[4]))
    rows = curserr.fetchall()

    for i in rows:
        print(i)
