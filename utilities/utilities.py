from pathlib import Path

from database.db_classes_niv import Years

"""
Arrange database information DATA UTILS
Parse databae query information DATA UTILS
"""


def get_project_root() -> Path:
    """Returns project root folder."""
    return Path(__file__).parent.parent


def ordered_verses_by_book(verses):
    ordered_verses = []

    x = range(1, 68)
    for n in x:
        for verse in verses:
            if n == verse.chapter.book_id:
                ordered_verses.append(verse)
    i = verses.count()
    ii = len(ordered_verses)
    return ordered_verses


def get_years_from_list(collection):
    all_years = []

    # loop through all the dictionaries in the list
    for l in collection:
        # get all years from the first to last
        all_years.append(l['first_year'])
        all_years.append(l['last_year'])

    return all_years


def years_convert_to_db_object(sorted_years):
    db_years = []

    # loop through the years
    for y in sorted_years:
        db_years.append(Years(year=y))

    return db_years

