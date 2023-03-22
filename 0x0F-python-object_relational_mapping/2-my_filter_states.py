#!/usr/bin/python3
"""Lists all states from database"""
if __name__ == "__main__":
    import sys
    import MySQLdb
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    name_srh = sys.argv[4]
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM states WHERE name LIKE '{name_srh}'\
    ORDER BY id ASC")
    rows = cursor.fetchall()
    for (id, name) in rows:
        print(f"({id}, '{name}')")
