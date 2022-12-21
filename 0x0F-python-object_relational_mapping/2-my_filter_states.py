#!/usr/bin/python3
"""
displays all values in state table where name matches
    user argument in database hbtn_0e_0_usa
Usage: ./2-my_filter_states.py <db_username> <db_password> <db_name>\
        <state to be found>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    query = "SELECT * FROM `states`\
            WHERE BINARY `name` = '{}'\
            ORDER BY states.id".format(sys.argv[4])
    c.execute(query)
    for state in c.fetchall():
        print(state)
