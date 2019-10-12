import os
import unittest
from calendar import TextCalendar
from datetime import datetime

from bi_classes.biblecalendar import BibleCalendar


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

    def convert_all_years_into_db_objects(self):
        calendar = BibleCalendar()
        list_of_700_years = calendar.get_desc_years_from(year=-4004)


if __name__ == '__main__':
    unittest.main()
