#!/usr/bin/python3
"""
This script prints all `State` objects containing the letter a
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    sn = Session()
    for s in sn.query(State).filter(State.name.like("%a%")).order_by(State.id):
        print("{}: {}".format(s.id, s.name))
