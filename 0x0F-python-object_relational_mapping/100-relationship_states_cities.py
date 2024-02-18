#!/usr/bin/python3

"""
the State “California”
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == "__main__":
    """ main function """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    newS = State(name='California')
    C = City(name='San Francisco')
    newS.cities.append(C)
    session.add(newS)
    session.commit()
    session.close()
