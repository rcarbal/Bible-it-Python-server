import os
import unittest
import json

from sqlalchemy import func
from database.databse_connection import DatabaseConnect
from database.db_classes_niv import Verse, Chapter, Book, Years, Civilization
from utilities.filereader_niv import get_all_bible_books, get_complete_bible
from utilities.matcher import get_bible_period
from utilities.utilities import get_project_root


class TestBibleitResults(unittest.TestCase):

    def test_retrieve_all_chapter(self):
        # connect to database
        root = get_project_root()
        db_path = os.path.join(root, 'database\\bibledatabase.db')
        database = DatabaseConnect(database='sqlite:///{}?check_same_thread=False'.format(db_path))
        database_session = database.session

        # get search by chapter
        results = database_session.query(Verse).filter_by(chapter_id=234).\
            join(Chapter)

        # loop through all that results that all verse id's equals 1
        for r in results:
            self.assertTrue(r.chapter.book.name == 'Genesis')

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

    def test_get_years_from_db(self):
        root = get_project_root()
        db_path = os.path.join(root, 'database\\bibledatabase.db')
        database = DatabaseConnect(database='sqlite:///{}?check_same_thread=False'.format(db_path))

        # retrieved all the odata for the period
        bible_periods = get_bible_period()

        # loop through all and get the id of the years
        for bp in bible_periods:
            # retrieve the first year and check databse
            first_year = bp['first_year']
            result = database.session.query(Years).filter(Years.year == first_year).one()
            result_id = result.year
            self.assertTrue(first_year == result_id)

    def test_check_civilization_object(self):
        root = get_project_root()
        db_path = os.path.join(root, 'database\\bibledatabase.db')
        database = DatabaseConnect(database='sqlite:///{}?check_same_thread=False'.format(db_path))
        civil_arr = []

        # retrieved all the data for the period
        bible_periods = get_bible_period()

        # loop through all period data and get the id of the years
        # to construct a Civilazition object
        for bp in bible_periods:
            # retrieve the first year and check databse
            first_year = bp['first_year']
            first_year_result = database.session.query(Years).filter(Years.year == first_year).one()
            # retrieve the second year and check the date
            last_year = bp['last_year']
            last_year_results = database.session.query(Years).filter(Years.year == last_year).one()

            if first_year_result.year == first_year and last_year_results.year == last_year:
                civil_arr.append(Civilization(position=bp['position'],
                                              name=bp['name'],
                                              first_year=first_year_result.id,
                                              last_year=last_year_results.id))

        # check that list is not empty
        self.assertTrue(len(civil_arr) > 4)



if __name__ == '__main__':
    unittest.main()
