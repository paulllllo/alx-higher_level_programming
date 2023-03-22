#!/usr/bin/python3
"""Lists all states from database"""
import sys
import MySQLdb
db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
cursor = db.cursor()
cursor.execute("SELECT * FROM states")
rows = cursor.fetchall()
for (id, name) in rows:
    print(f"({id}, '{name}')")
