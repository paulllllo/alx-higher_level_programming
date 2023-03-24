#!/usr/bin/python3
"""A script that lists all Cities"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   3306, sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state_name in session.query(City, State.name).join(State).\
            order_by(City.id.asc()):
        print(f"{state_name}: ({city.id}) {city.name}")
