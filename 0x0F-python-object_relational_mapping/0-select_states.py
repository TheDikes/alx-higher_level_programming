#!/usr/bin/python3
"""
Prints all states from the database name hbtn_0e_0usa
and take user, password and database as arguments
"""

import sys
import MySQLdb

if __name__ == '__main__':
db = MySQLdb.connect(
  host='localhost',
  port=3306,
  user=sys.argv[1],
  passwd=sys.argv[2],
  db=sys.argv[3])
cur = db.cursor()
cur.execute('SELECT * FROM states ORDER BY id ASC')

states = cursor.fetchall()
for state in states:
  print(state)
  cur.close()
  db.close()
