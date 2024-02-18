#!/usr/bin/python3
""" Lists State objects aa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)

    session = Session()

    for s in session.query(State).filter(State.name.contains('a')):
        print("{}: {}".format(s.id, s.name))

    session.close()
