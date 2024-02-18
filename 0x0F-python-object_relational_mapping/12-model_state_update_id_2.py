#!/usr/bin/python3
""" script lists all State objects """

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

    s = session.query(State).filter(State.id == 2).first()
    s.name = "New Mexico"
    session.commit()
    session.close()
