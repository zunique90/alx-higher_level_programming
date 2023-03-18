#!/usr/bin/env python3

import MySQLdb


db = MySQLdb.connect(
    host="localhost", port=3306, user="root", passwd="ezebuike",
    db="hbtn_0e_0_usa"
)
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
