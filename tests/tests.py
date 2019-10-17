import os
import unittest
import json

from sqlalchemy import func

from bi_classes.biblecalendar import BibleCalendar
from database.databse_connection import DatabaseConnect
from database.db_classes_niv import Verse, Chapter, Book, Years, GeneralBiblePeriods, HistoricalPeriods
from utilities.filereader_niv import get_all_bible_books, get_complete_bible
from utilities.matcher import get_bible_period, get_main_historical_periods
from utilities.utilities import get_project_root, convert_year_to_db


class TestBibleitResults(unittest.TestCase):

    def test_retrieve_all_chapter(self):
        # connect to database
        root = get_project_root()
        db_path = os.path.join(root, 'database\\bibledatabase.db')
        database = DatabaseConnect(database='sqlite:///{}?check_same_thread=False'.format(db_path))
        database_session = database.session

        # get search by chapter
        results = database_session.query(Verse).filter_by(chapter_id=234). \
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
                civil_arr.append(GeneralBiblePeriods(position=bp['position'],
                                                     name=bp['name'],
                                                     first_year=first_year_result.id,
                                                     last_year=last_year_results.id))

        # check that list is not empty
        self.assertTrue(len(civil_arr) > 4)

    def test_retrieve_periods(self):
        root = get_project_root()
        db_path = os.path.join(root, 'database\\bibledatabase.db')
        database = DatabaseConnect(database='sqlite:///{}?check_same_thread=False'.format(db_path))
        # retrieve database years
        years = database.session.query(Years).all()

        # get years
        cal = BibleCalendar()
        converted_to_bible_dates = cal.convert_int_to_cal_year(int_dates_list=years)

        # get Periods
        b_periods = database.session.query(GeneralBiblePeriods).all()

        # add civilization to year
        times = cal.append_bperiods_to_years(years=converted_to_bible_dates, bible_periods=b_periods)

        self.assertTrue(len(times) > 0)

    def test_retrieve_civilizations(self):
        root = get_project_root()
        db_path = os.path.join(root, 'database\\bibledatabase.db')
        database = DatabaseConnect(database='sqlite:///{}?check_same_thread=False'.format(db_path))
        # retrieve database years
        years = database.session.query(Years).all()

        # retrieve database of years
        cal = BibleCalendar()
        converted_to_bible_dates = cal.convert_int_to_cal_year(int_dates_list=years)

        # get Periods
        b_periods = database.session.query(GeneralBiblePeriods).all()

        # add civilization to year
        times = cal.append_bperiods_to_years(years=converted_to_bible_dates, bible_periods=b_periods)

        single_time_extrated = times[0]
        key_found = None

        if 'civ' in single_time_extrated:
            key_found = True
        else:
            key_found = False

        self.assertTrue(key_found)

    # retrieve all the years from the database
    def test_retrieve_all_database_yeasts(self):
        root = get_project_root()
        db_path = os.path.join(root, 'database\\bibledatabase.db')
        database = DatabaseConnect(database='sqlite:///{}?check_same_thread=False'.format(db_path))
        # retrieve database years
        years = database.session.query(Years).all()

        for year in years:
            print(year.year)

    def test_setup_historical_periods(self):
        print("Setting up Historical periods")
        root = get_project_root()
        db_path = os.path.join(root, 'database\\bibledatabase.db')
        database = DatabaseConnect(database='sqlite:///{}?check_same_thread=False'.format(db_path))
        periods = get_main_historical_periods()

        periods_list = []
        for p in periods:
            info = periods[p]

            # get first_year id
            first_year = database.session.query(Years).filter(Years.year == info['first_year']).first().id
            last_year = database.session.query(Years).filter(Years.year == info['last_year']).first().id

            periods_list.append(HistoricalPeriods(name=p, first_year_id=first_year, last_year_id=last_year))

        self.assertTrue(len(periods_list) > 0)


if __name__ == '__main__':
    unittest.main()
