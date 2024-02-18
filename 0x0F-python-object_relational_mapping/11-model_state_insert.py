#!/usr/bin/python3
""" define State class """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)

    session = Session()
    s = State(name='Louisiana')
    session.add(s)
    session.commit()
    print('{0}'.format(s.id))
    session.close()
