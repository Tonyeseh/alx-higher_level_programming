#!/usr/bin/python3
"""
prints state object with name passed as arg from database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State)

    printed = False
    for state in states:
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            printed = True
    if printed is False:
        print("Not found")
    Base.metadata.create_all(engine)
