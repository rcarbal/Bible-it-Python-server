from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Years(Base):
    __tablename__ = 'years'

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)