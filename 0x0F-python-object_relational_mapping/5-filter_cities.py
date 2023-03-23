#!/usr/bin/python3
"""Lists all cities from database that match a state passed
 in the command line arg"""
if __name__ == "__main__":
    import sys
    import MySQLdb
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    name_srch = ""
    if (all([char not in sys.argv[4] for char in ["\\", "\'", "\""]])):
        name_srch = sys.argv[4]
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities JOIN states \
    ON cities.state_id = states.id \
    WHERE states.name LIKE BINARY '{}'\
    ORDER BY cities.id ASC".format(name_srch))
    rows = cursor.fetchall()
    name_list = []
    for row in rows:
        name_list.append(row[0])
    print(", ".join(name_list))
