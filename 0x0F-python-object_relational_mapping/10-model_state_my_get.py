#!/usr/bin/python3
""" Lists State objects"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)

    session = Session()

    s = session.query(State).filter(State.name == argv[4]).first()

    if s is None:
        print('Not found')
    else:
        print('{0}'.format(s.id))
