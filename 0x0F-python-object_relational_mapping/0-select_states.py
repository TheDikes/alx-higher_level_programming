#!/usr/bin/python3
""" This script lists all states from the database hbtn_0e_0usa 
   and it takes 3 arguments: username, password and database 
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost', 
            port=3306, 
            user=sys.argv[1], 
            passwd=sys.argv[2], 
            dbase=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
