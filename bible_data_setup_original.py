import sys
import pdb
# for use on windows pycharm
import database
from database.db_classes_niv import BibleSection, Verse, Years

# for use on linux
# import db_classes_niv
# from db_classes_niv import BibleSection, Book, Verse, Chapter, Years


# sys.path.insert(0, '/vagrant/Bible-it-Server')
import utilities

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from utilities.db_converter import convert_section_list_to_book_db, convert_book_list_to_db, convert_verses_list_to_db
from utilities.filereader_niv import get_complete_bible, get_all_bible_books
from utilities.matcher import match_books_to_section, get_bible_period, get_civilization
from utilities.utilities import get_years_from_list, years_convert_to_db_object





Base = declarative_base()


# Run this file 1st in order.

def setup_bible_db():
    # add_years_to_db()
    add_bible_sections_to_db()
    add_books_to_db()
    add_chapters_to_db()
    add_verses_to_db()


def add_years_to_db():
    print("Initiate Save Years to database")
    # get all the years
    all_years = []
    bible_period = get_bible_period()

    general_biblical_periods = get_years_from_list(collection=bible_period)
    all_years.extend(general_biblical_periods)

    civilization = get_civilization()

    civilizations = get_years_from_list(collection=civilization)
    all_years.extend(civilizations)

    # remove duplicates
    no_duplicates = list(dict.fromkeys(all_years))

    # sort the years from oldest to newest
    sorted_years = sorted(no_duplicates, key=int, reverse=False)
    print(sorted_years)

    # save timeline data to database
    years_db_object = years_convert_to_db_object(sorted_years=sorted_years)
    session.add_all(years_db_object)
    session.commit()
    print("Years added to database")


def add_bible_sections_to_db():
    print("Setting up Sections Database")
    old_testament = BibleSection(name="Old Testament")
    new_testament = BibleSection(name="New Testament")

    section_list = [old_testament, new_testament]
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
    # db_classes_niv.instance()

    # 2Qepxniw-setup-database
    command = input("Command: ")

    if command == 'a':
        print("Setting Up Database NIV")
        setup_bible_db()


if __name__ == '__main__':
    engine = create_engine('sqlite:///database/bibledatabase.db?check_same_thread=False', echo=False)
    Base.metadata.create_all(engine)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    run_command()
