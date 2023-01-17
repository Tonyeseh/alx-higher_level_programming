#!/usr/bin/python3
"""
displays all values in state table where name matches
    user argument in database hbtn_0e_0_usa
safe from sql injection
Usage: ./2-my_safe_filter_states.py <db_username> <db_password> <db_name>\
        <state to be found>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    query = "SELECT * FROM `states`"
    c.execute(query)
    for state in c.fetchall():
        if state[1] == sys.argv[4]:
            print(state)
