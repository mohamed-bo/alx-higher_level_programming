#!/usr/bin/python3
""" script lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == '__main__':
    """
    function
    """
    db = MySQLdb.connect(host='localhost', user=sys.argv[1], port=3306,
                         db=sys.argv[3], passwd=sys.argv[2])

    curserr = db.cursor()
    curserr.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")
    rows = curserr.fetchall()
    for row in rows:
        print(row)
    curserr.close()
    db.close()
