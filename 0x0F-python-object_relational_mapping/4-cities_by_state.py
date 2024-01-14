#!/usr/bin/python3
"""
list all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cursr = db.cursor()
    cursr.execute("""SELECT cities.id, cities.name, states.name FROM
        cities INNER JOIN states ON states.id=cities.state_id""")
    records = cursr.fetchall()
    for record in records:
        print(record)

    cursr.close()
    db.close()
