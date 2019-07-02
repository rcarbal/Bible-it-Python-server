from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database.db_setup_niv import Book, BibleSection

Base = declarative_base()

engine = create_engine('sqlite:///bibledatabase.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def convert_list_to_book_db(list_of_books, section):
    bible_section = None

    if section == 0:
        bible_section = session.query(BibleSection).filter_by(name='Old Testament')
    elif section == 1:
        bible_section = session.query(BibleSection).filter_by(name='New Testament')
    list = []

    for book in list_of_books:
        list.append(Book())
