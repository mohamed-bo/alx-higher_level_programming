#!/usr/bin/python3
""" script lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    """ main function """
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         host="localhost", port=3306,
                         db=sys.argv[3])
    crusorr = db.cursor()
    crusorr.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                    (sys.argv[4],))
    rows = crusorr.fetchall()
    for i in rows:
        print(i)
    crusorr.close()
    db.close()
