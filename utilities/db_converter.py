from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database.db_setup_niv import Book, BibleSection

Base = declarative_base()

engine = create_engine('sqlite:///bibledatabase.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def convert_list_to_book_db(old_testament, new_testament):

    old = session.query(BibleSection).filter_by(name="Old Testament").first()
    new = session.query(BibleSection).filter_by(name='New Testament').first()
    list = []

    for book in old_testament:
        list.append(Book(name=book, section_id=old.id))

    for book in new_testament:
        list.append(Book(name=book, section_id=new.id))

    return list
