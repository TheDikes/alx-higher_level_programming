#!/usr/bin/python3
"""
Prints all states from the database hbtn_0e_0_usa
and take user, password and database name as arguments
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
    cur.execute('SELECT * FROM states ORDER BY id ASC')

    states = cur.fetchall()
    for state in states:
        print(state)
        cur.close()
        db.close()
