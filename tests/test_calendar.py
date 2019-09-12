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
        current_year = datetime.now().year
        list_of_700_years = calendar.get_desc_years_from(year=7000)
        earliest_year = list_of_700_years[-1]

        self.assertTrue(-4980 == earliest_year)


if __name__ == '__main__':
    unittest.main()
