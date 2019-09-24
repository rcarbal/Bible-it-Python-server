from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

'''
Standard connection to be used anywhere in the application
'''

class DatabaseConnect(object):
    def __init__(self, database):
        Base = declarative_base()
        engine = create_engine(database, echo=False)
        Base.metadata.create_all(engine)
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        self._session = session

    @property
    def session(self):
        return self._session
