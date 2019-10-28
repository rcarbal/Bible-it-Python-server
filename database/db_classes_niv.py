from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

'''
SQLAlchemy classes to be used in main script file so to not run into Spacy windows compiler error
'''


class BibleSection(Base):
    __tablename__ = 'section'

    id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    section_id = Column(Integer, ForeignKey('section.id'))
    section = relationship(BibleSection)


class Chapter(Base):
    __tablename__ = "chapter"
    id = Column(Integer, primary_key=True)
    chapter = Column(String, nullable=False)
    book_id = Column(Integer, ForeignKey('book.id'))
    book = relationship(Book)


class Verse(Base):
    __tablename__ = "verse"

    id = Column(Integer, primary_key=True)
    verse_number = Column(String(10), nullable=False)
    verse_string = Column(String(1000), nullable=False)
    chapter_id = Column(Integer, ForeignKey('chapter.id'))
    chapter = relationship(Chapter)


class Years(Base):
    __tablename__ = 'years'

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)


class GeneralBiblePeriods(Base):
    __tablename__ = 'bible_periods'

    id = Column(Integer, primary_key=True)
    position = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    first_year_id = Column(Integer, ForeignKey('years.id'), nullable=False)
    last_year_id = Column(Integer, ForeignKey('years.id'), nullable=False)


class HistoricalPeriods(Base):
    __tablename__ = 'historical_periods'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    first_year_id = Column(Integer, ForeignKey('years.id'), nullable=False)
    last_year_id = Column(Integer, ForeignKey('years.id'), nullable=False)

class BiblibicalFigures(Base):
    __tablename__ = 'biblical_figures'

    id = Column(Integer, primary_key=True)
    gender = Column(String, nullable=True)
    name = Column(String, nullable=False)
    born_id = Column(Integer, ForeignKey('years.id'), nullable=False)
    died_id = Column(Integer, ForeignKey('years.id'), nullable=False)
    is_born_estimated = Column(Boolean, nullable=True)
    is_death_estimated = Column(Boolean, nullable=True)
    father = Column(Integer, nullable=True)
    mother = Column(Integer, nullable=True)
    sons = Column(Integer, nullable=True)
    daughters = Column(Integer, nullable=True)
    lifespan = Column(Integer, nullable=True)

