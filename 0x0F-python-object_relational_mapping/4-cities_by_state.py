#!/usr/bin/python3
"""
Takes in 3 args and lists all cities from db hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM `cities` \
            INNER JOIN states\
            ON cities.state_id = states.id\
            ORDER BY cities.id")
    for city in c.fetchall():
        print(city)
