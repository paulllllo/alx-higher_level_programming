#!/usr/bin/python3
"""A script that updates a row in a table"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   3306, sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).filter(State.id == 2).\
        update({'name': "New Mexico"})
    session.commit()
