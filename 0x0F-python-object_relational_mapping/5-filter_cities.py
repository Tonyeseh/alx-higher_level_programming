#!/usr/bin/python3
"""
Takes in 4 args and lists all cities from db hbtn_0e_4_usa
+ that matches with fourth arg
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
    cities = []
    for city in c.fetchall():
        if city[2] == sys.argv[4]:
            cities.append(city[1])
    print(", ".join(cities))
