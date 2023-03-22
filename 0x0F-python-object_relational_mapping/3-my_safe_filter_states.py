#!/usr/bin/python3
"""Lists all states from database that match a command line arg"""
if __name__ == "__main__":
    import sys
    import MySQLdb
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    name_srch = ""
    if not (all([char in sys.argv[4] for char in ["\\", "\'", "\""]])):
        name_srch = sys.argv[4]
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
    ORDER BY id ASC".format(name_srch))
    rows = cursor.fetchall()
    for (id, name) in rows:
        print(f"({id}, '{name}')")
