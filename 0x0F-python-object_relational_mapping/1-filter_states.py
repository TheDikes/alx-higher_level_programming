#!/usr/bin/python3
"""
Prints all states that starts with N(upper N)
"""

import sys
import MySQLdb

if __name__ == '__main__':
  db = MySQLdb.connect(
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3],
    port=3306,
    host='localhost')
  cur = db.cursor()
  cur.execute('SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC')
  
  states = cursor.fetchall()
  
  for state in states:
    print(state)
    cur.close()
    db.close()
