#!/usr/bin/python3
""" Lists first State object"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """main function"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)

    session = Session()

    if s is None:
        print('Nothing')
    else:
        print('{0}: {1}'.format(s.id, s.name))

    session.close()
