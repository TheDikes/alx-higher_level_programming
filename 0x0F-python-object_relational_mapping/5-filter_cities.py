#!/usr/bin/python3
"""  Takes the name of a state as an argument 
     and lists all cities of the state from the database hbtn_0e_0_usa 
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    city = (sys.argv[4], )
    query = '''SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name = %s ORDER BY cities.id ASC'''
    cur.execute(query, city)
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
