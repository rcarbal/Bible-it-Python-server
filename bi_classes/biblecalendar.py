from datetime import datetime, timedelta


class BibleCalendar(object):

    def __init__(self):
        pass

    # returns current year in with BC ir AD
    @staticmethod
    def get_year_now():

        year = datetime.now().year
        return '{} AD'.format(year)

    @staticmethod
    def get_desc_years_from(year):
        years = []
        current = datetime.now().year
        desc_years = range(year)

        # loop backwards
        for i in desc_years:

            # convert to biblical year
            if current > 0:
                # year = '{} AD'.format(current)
                years.append(current)
            elif current < 0:
                # remove_negativity = current * -1
                # year = '{} BC'.format(remove_negativity)
                years.append(current)

            # remove 1 year from current
            current = current - 1

        return years
