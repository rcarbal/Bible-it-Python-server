from database.databse_connection import DatabaseConnect
from database.db_classes_niv import Verse
from utilities.word_process import retrieve_all_pos_in_verse
import json


def build_dictionary_verse_query(verse):
    verse_dictionary = {
        'verse_number': verse.verse_number,
        'chapter_number': verse.chapter.chapter,
        'book_id': verse.chapter.book_id
    }

    return verse_dictionary


def build_dictionary_book_query(book):
    book_dictionary = {
        'book_name': book.name,
        'section_name': book.section.name
    }
    return book_dictionary


def retrieve_all_pos():
    database = DatabaseConnect(database='sqlite:///bibledatabase.db?check_same_thread=False')
    verses = database.session.query(Verse).all()

    # retrieve all the pos in the verses into a list
    list_pos = []
    for verse in verses:
        all_pos_in_verse = retrieve_all_pos_in_verse(verse.verse_string)
        list_pos.extend(all_pos_in_verse)

    # use Frozenset to remove duplicates
    fset = frozenset(list_pos)
    for f in fset:
        print('["{}",""],'.format(f))


def get_bible_string():
    data = None
    bible_string = json.dumps(data)
    return bible_string
