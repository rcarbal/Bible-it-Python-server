from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database.db_setup_niv import BibleSection, Book
from utilities.db_converter import convert_list_to_book_db
from utilities.filereader_niv import get_complete_bible, get_all_bible_books
from utilities.matcher import match_books_to_section

Base = declarative_base()

engine = create_engine('sqlite:///bibledatabase.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def setup_bible_section_db():
    old_testament = BibleSection(name="Old Testament")
    new_tesament = BibleSection(name="New Testament")

    section_list = [old_testament, new_tesament]
    session.add_all(section_list)
    session.commit()


def add_books_to_db():
    books_sectioned_off = match_books_to_section()
    old_testament = books_sectioned_off[0]['OLD TESTAMENT']
    new_testament = books_sectioned_off[1]['NEW TESTAMENT']

    list_old_testament_db = convert_list_to_book_db(old_testament, 0)

add_books_to_db()
