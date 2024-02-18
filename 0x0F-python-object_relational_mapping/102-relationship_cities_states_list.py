#!/usr/bin/python3


"""
lists all State objects
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    resultat = session.query(State).join(City).order_by(City.id).all()

    for s in resultat:
        for c in s.cities:
            print("{}: {} -> {}".format(c.id, c.name, s.name))
