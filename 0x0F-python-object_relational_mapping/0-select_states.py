#!/usr/bin/python3
"""
lists all states from the databasse hbtn_0e_0_usa
Usage: ./0-select_states.py <db_username> <db_password> <db_name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY states.id")
    for state in c.fetchall():
        print(state)
