#!/usr/bin/python3
""" prints all City objects"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == '__main__':
    """ main function """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City, State).join(State)
    for city, state in result.all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()
