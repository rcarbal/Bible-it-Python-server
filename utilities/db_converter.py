from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database.db_classes_niv import Book, BibleSection, Chapter, Verse
from nlp.bibleit_NLP import getSpacyVerse
from utilities.filereader_niv import get_book_from_bible, get_complete_bible

import datetime

Base = declarative_base()

engine = create_engine('sqlite:///bibledatabase.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def convert_section_list_to_book_db(old_testament, new_testament):
    old = session.query(BibleSection).filter_by(name="Old Testament").first()
    new = session.query(BibleSection).filter_by(name='New Testament').first()
    list = []

    for book in old_testament:
        list.append(Book(name=book, section_id=old.id))

    for book in new_testament:
        list.append(Book(name=book, section_id=new.id))

    return list


def convert_book_list_to_db(bible, book_list):
    chapters = []

    for book in book_list:
        retieved_book = bible.get(book)

        db_book = session.query(Book).filter_by(name=book).first()
        for key in retieved_book.keys():
            chapters.append(Chapter(chapter=key, book_id=db_book.id))

    return chapters


def convert_verses_list_to_db(books):
    verse_list = []
    bible = get_complete_bible()
    verse_index_count = 0

    print(datetime.datetime.now())
    for book in books:
        book = session.query(Book).filter_by(name=book).first()

        # All book chapters in file.
        book_in_file = get_book_from_bible(bible, book.name)

        # All Book Chapters in the database
        db_chapters_in_book = session.query(Chapter).filter_by(book_id=book.id).all()

        for chapter in book_in_file:
            # Chapter in the file with verses
            file_chapter_verses = book_in_file[chapter]
            parsed_db_chapter_id = find_db_chapter_from_parse(db_chapters_in_book, chapter)

            for verse in file_chapter_verses:
                # verse String
                parsed_versed = file_chapter_verses[verse]

                # Convert verse into JSON  Spacy Break down
                spacy_verse = getSpacyVerse(parsed_versed, verse_index_count)

                verse_list.append(
                    Verse(verse_number=verse, verse_string=spacy_verse, chapter_id=parsed_db_chapter_id))
                verse_index_count += 1

    print(datetime.datetime.now())

    return verse_list


def find_db_chapter_from_parse(db_chapters, file_chapter):
    for db_chapter in db_chapters:
        if file_chapter == db_chapter.chapter:
            return db_chapter.id
