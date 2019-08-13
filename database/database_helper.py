from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database.db_setup_niv import BibleSection, Book, Verse, Chapter
from utilities.db_converter import convert_section_list_to_book_db, convert_book_list_to_db, convert_verses_list_to_db
from utilities.filereader_niv import get_complete_bible, get_all_bible_books
from utilities.matcher import match_books_to_section

from database import db_setup_niv

Base = declarative_base()


def setup_bible_db():
    add_bible_sections_to_db()
    add_books_to_db()
    add_chapters_to_db()
    add_verses_to_db()


def add_bible_sections_to_db():
    print("Setting up Sections Database")
    old_testament = BibleSection(name="Old Testament")
    new_tesament = BibleSection(name="New Testament")

    section_list = [old_testament, new_tesament]
    session.add_all(section_list)
    session.commit()
    print("Committed Sections Database")


def add_books_to_db():
    print("Setting up Books Database")
    books_sectioned_off = match_books_to_section()
    old_testament = books_sectioned_off[0]['OLD TESTAMENT']
    new_testament = books_sectioned_off[1]['NEW TESTAMENT']

    list_old_testament_db = convert_section_list_to_book_db(old_testament, new_testament)
    session.add_all(list_old_testament_db)
    session.commit()
    print("Committed Books Database")


def add_chapters_to_db():
    print("Setting up Chapters Database")
    bible = get_complete_bible()
    books = get_all_bible_books(bible)
    chapters = convert_book_list_to_db(bible, books)

    session.add_all(chapters)
    session.commit()
    print("Committed Chapters Database")


def add_verses_to_db():
    print("Setting up Verses Database")
    bible = get_complete_bible()
    books = get_all_bible_books(bible)
    verses = convert_verses_list_to_db(books)

    session.add_all(verses)
    session.commit()
    print("Committed Verses Database")


def parse_word_db(word):
    pass


def get_verses():
    verses = session.query(Verse).all()
    for verse in verses:
        print(verse.verse_string)


def run_command():
    db_setup_niv.run_main()

    # 2Qepxniw-setup-database
    command = input("Command: ")

    if command == '2Qepxniw-setup-database':
        print("Setting Up Database NIV")
        setup_bible_db()


if __name__ == '__main__':
    # Base = declarative_base()
    # engine = create_engine('sqlite:///bibledatabase.db?check_same_thread=False', echo=True)
    # Base.metadata.create_all(engine)
    # DBSession = sessionmaker(bind=engine)
    # session = DBSession()

    engine = create_engine('sqlite:///bibledatabase.db')
    Base.metadata.create_all(engine)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    run_command()
