#!/usr/bin/python3
""" sciprt list all cities from the database hbtn_0e_4_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    """ main function """
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         host="localhost", port=3306,
                         db=sys.argv[3])
    cursetr = db.cursor()
    cursetr.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")
    rows = cursetr.fetchall()
    for i in rows:
        print(i)
    cursetr.close()
    db.close()
