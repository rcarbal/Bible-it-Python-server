import os
import unittest
import json

from database.databse_connection import DatabaseConnect
from database.db_classes_niv import Verse
from utilities.filereader_niv import get_all_bible_books, get_complete_bible


class TestBibleitResults(unittest.TestCase):

    def test_retrieve_niv_books(self):
        complete_bible = get_complete_bible()
        all_the_bible_books = get_all_bible_books(complete_bible)
        print('{} books where found'.format(len(all_the_bible_books)))
        self.assertTrue(len(all_the_bible_books) == 66)

    def test_results_from_db(self):
        db_path = os.path.join(os.path.dirname(__file__), '..\\database\\bibledatabase.db')
        print(db_path)
        database = DatabaseConnect(database='sqlite:///{}?check_same_thread=False'.format(db_path))
        verses = database.session.query(Verse).all()
        index = 0
        for verse in verses:
            index += 1
            print(verse.verse_string)

        self.assertTrue(index > 1)


if __name__ == '__main__':
    unittest.main()
