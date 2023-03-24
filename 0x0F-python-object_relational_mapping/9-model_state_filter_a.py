#!/usr/bin/python3
"""A script that lists all States filtering for those containing 'a'"""
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
    instances = session.query(State).order_by(State.id.asc())\
                .filter(State.name.like('%a%'))
    for instance in instances:
        print(f"{instance.id}: {instance.name}")
