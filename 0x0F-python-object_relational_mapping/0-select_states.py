#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    """ lists all states from the database hbtn_0e_0_usa """

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    curserr = db.cursor()
    curserr.execute("SELECT * FROM states")
    rows = curserr.fetchall()
    for row in rows:
        print(row)
    curserr.close()
    db.close()
