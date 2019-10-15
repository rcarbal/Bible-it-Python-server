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
        desc_years = range(year, current+1)



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

    @staticmethod
    def convert_int_to_cal_year(int_dates_list):
        return_dates = []

        if int_dates_list is not None:
            for i in int_dates_list:
                y = {}
                if i.year < 0:
                    remove_negativity = i.year * -1
                    y['year'] = "{} BC".format(remove_negativity)
                    y['id'] = i.id
                    return_dates.append(y)

                elif i.year > 0:
                    y['year'] = "{} AD".format(i.year)
                    y['id'] = i.id
                    return_dates.append(y)

        return return_dates

    @staticmethod
    def append_bperiods_to_years(years, bible_periods):
        complete = []
        periods = {}

        # extract all the civilization data
        for c in bible_periods:
            periods[str(c.position)] = c

        # loop through the years and get any period that has reference to that year
        for y in years:
            year_id = y['id']

            # check all the periods for reference to year
            for p in periods:
                period = periods[p]
                if period.first_year_id == year_id:
                    y['period'] = period.name
                    complete.append(y)

        return complete
