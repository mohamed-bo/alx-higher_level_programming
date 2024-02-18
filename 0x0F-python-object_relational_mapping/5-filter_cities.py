#!/usr/bin/python3
"""script list all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ main function """
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         host="localhost", port=3306,
                         db=sys.argv[3])
    cursser = db.cursor()
    cursser.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4]))
    rows = cursser.fetchall()
    if rows is not None:
        print(", ".join([row[0] for row in rows]))
    cursser.close()
    db.close()
