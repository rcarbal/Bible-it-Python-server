import os
import unittest
from calendar import TextCalendar
from datetime import datetime

from bi_classes.biblecalendar import BibleCalendar
from utilities.utilities import convert_year_to_db


class TestCalendar(unittest.TestCase):

    def test_calendar_years(self):
        calendar = BibleCalendar()
        year = calendar.get_year_now()
        print(year)

        self.assertTrue('AD' in year)

    def test_get_year_range_7000_years_ago(self):
        calendar = BibleCalendar()
        list_of_700_years = calendar.get_desc_years_from(year=-4004)
        # convert the years into Year database object
        last_year = list_of_700_years[0]
        first_year = list_of_700_years.pop()

        self.assertTrue(first_year == -4004 and last_year == 2019)

        list_of_700_years.reverse();

        revered_first = list_of_700_years[0]
        reversed_last = list_of_700_years.pop()

        self.assertTrue(revered_first == -4003 and reversed_last == 2019)

    def test_convert_all_years_into_db_objects(self):
        # get a list of all the years
        calendar = BibleCalendar()
        list_of_700_years = calendar.get_desc_years_from(year=-4004)

        # convert years into db items
        list_of_db_items = convert_year_to_db(years_list=list_of_700_years)

        # check that the list length is the same as the length of the year list
        year_list_length = len(list_of_700_years)

        db_list_length = len(list_of_db_items)

        self.assertTrue(year_list_length == db_list_length)


if __name__ == '__main__':
    unittest.main()
