#!/usr/bin/python3
"""script that lists all states from a database"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2],
        db=argv[3], charset="utf8"
    )
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                    INNER JOIN states ON cities.state_id = states.id\
                    WHERE states.name = '{:s}'\
                    ORDER BY cities.id ASC".format(argv[4]))
    rows = cur.fetchall()
    res = []
    for row in rows:
        res.append(row[0])
    print(", ".join(res))
    cur.close()
    db.close()
