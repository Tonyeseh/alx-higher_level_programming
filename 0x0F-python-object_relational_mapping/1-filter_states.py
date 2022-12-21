#!/usr/bin/python3
"""
lists all states with name starting with `N` from the database hbtn_0e_0_usa
Usage: ./1-filter_states.py <db_username> <db_password> <db_name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` WHERE `name` LIKE 'N%'")
    for state in c.fetchall():
        print(state)
