"""Class definition of a state with declaration of base"""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'\
                       .format("root", "root", 3306, "hbtn_0e_4_usa"))
Base = declarative_base()
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True, \
                autoincrement=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return "<User(name='%s')>" % (self.name)
#Base.metadata.create_all(engine)
