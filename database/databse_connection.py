from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///bibledatabase.db?check_same_thread=False', echo=False)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


class DatabaseConnect(object):
    def __init__(self):
        self._session = session

    @property
    def session(self):
        return self._session


if __name__ == '__main__':
    pass
