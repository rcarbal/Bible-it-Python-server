import os
import unittest
import json

from sqlalchemy import func

from constants.static import BOOK_ORDER
from database.databse_connection import DatabaseConnect
from database.db_classes_niv import Verse, Chapter, Book
from utilities.filereader_niv import get_all_bible_books, get_complete_bible
from utilities.utilities import get_project_root


class TestBibleitResults(unittest.TestCase):

    def test_random_stuff(self):
        x = range(1,68)
        for n in x:
            print(n)

    def test_retrieve_niv_books(self):
        complete_bible = get_complete_bible()
        all_the_bible_books = get_all_bible_books(complete_bible)
        print('{} books where found'.format(len(all_the_bible_books)))
        self.assertTrue(len(all_the_bible_books) == 66)

    def test_retrieve_books_in_order(self):
        # connect to database
        root = get_project_root()
        db_path = os.path.join(root, 'database\\bibledatabase.db')
        database = DatabaseConnect(database='sqlite:///{}?check_same_thread=False'.format(db_path))

    def tes_count_verses_from_db(self):
        root = get_project_root()
        db_path = os.path.join(root, 'database\\bibledatabase.db')
        database = DatabaseConnect(database='sqlite:///{}?check_same_thread=False'.format(db_path))
        verses = database.session.query(Verse).all()
        index = 0
        for verse in verses:
            index += 1

        self.assertTrue(index == 31102)


if __name__ == '__main__':
    unittest.main()
