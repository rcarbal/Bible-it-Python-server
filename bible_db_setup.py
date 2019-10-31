import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from bi_classes.biblecalendar import BibleCalendar
from nlp.bibleit_NLP import getSpacyVerse
from utilities.filereader_niv import get_complete_bible, get_all_bible_books, get_book_from_bible
from utilities.matcher import get_bible_period, get_civilization, match_books_to_section, get_main_historical_periods, \
    get_biblical_figures
from utilities.utilities import convert_year_to_db

'''
Main database setup script to be run in vagrant environment.
'''

Base = declarative_base()


class BibleSection(Base):
    __tablename__ = 'section'

    id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    section_id = Column(Integer, ForeignKey('section.id'))
    section = relationship(BibleSection)


class Chapter(Base):
    __tablename__ = "chapter"
    id = Column(Integer, primary_key=True)
    chapter = Column(String, nullable=False)
    book_id = Column(Integer, ForeignKey('book.id'))
    book = relationship(Book)


class Verse(Base):
    __tablename__ = "verse"

    id = Column(Integer, primary_key=True)
    verse_number = Column(String(10), nullable=False)
    verse_string = Column(String(1000), nullable=False)
    chapter_id = Column(Integer, ForeignKey('chapter.id'))
    chapter = relationship(Chapter)


class Years(Base):
    __tablename__ = 'years'

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)


class GeneralBiblePeriods(Base):
    __tablename__ = 'bible_periods'

    id = Column(Integer, primary_key=True)
    position = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    first_year_id = Column(Integer, ForeignKey('years.id'), nullable=False)
    last_year_id = Column(Integer, ForeignKey('years.id'), nullable=False)


class HistoricalPeriods(Base):
    __tablename__ = 'historical_periods'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    first_year_id = Column(Integer, ForeignKey('years.id'), nullable=False)
    last_year_id = Column(Integer, ForeignKey('years.id'), nullable=False)


class BiblibicalFigures(Base):
    __tablename__ = 'biblical_figures'

    id = Column(Integer, primary_key=True)
    gender = Column(String, nullable=True)
    name = Column(String, nullable=False)
    born_id = Column(Integer, ForeignKey('years.id'), nullable=False)
    died_id = Column(Integer, ForeignKey('years.id'), nullable=False)
    is_born_estimated = Column(Boolean, nullable=True)
    is_death_estimated = Column(Boolean, nullable=True)
    father = Column(Integer, nullable=True)
    mother = Column(Integer, nullable=True)
    sons = Column(Integer, nullable=True)
    daughters = Column(Integer, nullable=True)
    lifespan = Column(Integer, nullable=True)


engine = create_engine('sqlite:///database/bibledatabase.db?check_same_thread=False', echo=False)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def setup_bible_db():
    add_period_years_to_db()
    setup_db_bible_general_periods()
    add_historical_periods()
    add_bible_sections_to_db()
    add_books_to_db()
    add_chapters_to_db()
    add_verses_to_db()
    add_biblical_figures()


# methods to setup database
# Adds only the years as they relate to periods.
def add_period_years_to_db():
    print("Initiate Save Years to database")
    # get a list of all the years
    calendar = BibleCalendar()
    list_of_700_years = calendar.get_desc_years_from(year=-4004)

    # convert years into db items
    years_db_object = convert_year_to_db(years_list=list_of_700_years)
    years_db_object.reverse()

    session.add_all(years_db_object)
    session.commit()
    print("Years added to database")


def setup_db_bible_general_periods():
    civil_arr = []

    # retrieved all the data for the period
    bible_periods = get_bible_period()

    # loop through all period data and get the id of the years
    # to construct a Civilazition object
    for bp in bible_periods:
        # retrieve the first year and check databse
        first_year = bp['first_year']
        first_year_result = session.query(Years).filter(Years.year == first_year).one()
        # retrieve the second year and check the date
        last_year = bp['last_year']
        last_year_results = session.query(Years).filter(Years.year == last_year).one()

        if first_year_result.year == first_year and last_year_results.year == last_year:
            civil_arr.append(GeneralBiblePeriods(position=bp['position'],
                                                 name=bp['name'],
                                                 first_year_id=first_year_result.id,
                                                 last_year_id=last_year_results.id))

    # save to database
    session.add_all(civil_arr)
    session.commit()


def add_historical_periods():
    print("Setting up Historical periods")
    periods = get_main_historical_periods()

    periods_list = []
    for p in periods:
        info = periods[p]

        # get first_year id
        first_year = session.query(Years).filter(Years.year == info['first_year']).first().id
        last_year = session.query(Years).filter(Years.year == info['last_year']).first().id

        periods_list.append(HistoricalPeriods(name=p, first_year_id=first_year, last_year_id=last_year))

    # save to database
    session.add_all(periods_list)
    session.commit()


def add_bible_sections_to_db():
    print("Setting up Sections Database")
    old_testament = BibleSection(name="Old Testament")
    new_testament = BibleSection(name="New Testament")

    section_list = [old_testament, new_testament]
    session.add_all(section_list)
    session.commit()
    print("Committed Sections Database")


def add_books_to_db():
    print("Setting up Books Database")
    books_sectioned_off = match_books_to_section()
    old_testament = books_sectioned_off[0]['OLD TESTAMENT']
    new_testament = books_sectioned_off[1]['NEW TESTAMENT']

    list_old_testament_db = convert_section_list_to_book_db(old_testament, new_testament)
    session.add_all(list_old_testament_db)
    session.commit()
    print("Committed Books Database")


def add_chapters_to_db():
    print("Setting up Chapters Database")
    bible = get_complete_bible('bible-json/NIV.json')
    books = get_all_bible_books(bible)
    chapters = convert_book_list_to_db(bible, books)

    session.add_all(chapters)
    session.commit()
    print("Committed Chapters Database")


def add_verses_to_db():
    print("Setting up Verses Database")
    bible = get_complete_bible('bible-json/NIV.json')
    books = get_all_bible_books(bible)
    verses = convert_verses_list_to_db(books)

    session.add_all(verses)
    session.commit()
    print("Committed Verses Database")


def add_biblical_figures():
    print("Adding biblical figures")
    figures = get_biblical_figures()

    figures_list = []
    for f in figures:
        gender = f['gender']
        name = f['name']
        born = f['year_born']
        died = f['year_died']

        # get first_year id
        born_id = session.query(Years).filter(Years.year == born).first().id
        died_id = session.query(Years).filter(Years.year == died).first().id

        figures_list.append(BiblibicalFigures(gender=gender,
                                              name=name,
                                              born_id=born_id,
                                              died_id=died_id))

    session.add_all(figures_list)
    session.commit()


def convert_section_list_to_book_db(old_testament, new_testament):
    old = session.query(BibleSection).filter_by(name="Old Testament").first()
    new = session.query(BibleSection).filter_by(name='New Testament').first()
    list = []

    for book in old_testament:
        list.append(Book(name=book, section_id=old.id))

    for book in new_testament:
        list.append(Book(name=book, section_id=new.id))

    return list


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


def convert_book_list_to_db(bible, book_list):
    chapters = []

    for book in book_list:
        retieved_book = bible.get(book)

        db_book = session.query(Book).filter_by(name=book).first()
        for key in retieved_book.keys():
            chapters.append(Chapter(chapter=key, book_id=db_book.id))

    return chapters


def convert_verses_list_to_db(books):
    verse_list = []
    bible = get_complete_bible('bible-json/NIV.json')
    verse_index_count = 0

    print(datetime.datetime.now())
    for book in books:
        # pdb.set_trace()
        book_retreived = session.query(Book).filter_by(name=book).first()

        # All book chapters in file.
        book_in_file = get_book_from_bible(bible, book_retreived.name)

        # All Book Chapters in the database
        db_chapters_in_book = session.query(Chapter).filter_by(book_id=book_retreived.id).all()

        for chapter in book_in_file:
            # Chapter in the file with verses
            file_chapter_verses = book_in_file[chapter]
            parsed_db_chapter_id = find_db_chapter_from_parse(db_chapters_in_book, chapter)

            for verse in file_chapter_verses:

                verse_number = None
                if len(verse) == 1:
                    verse_number = '0{}'.format(verse)
                else:
                    verse_number = verse
                # verse String
                parsed_versed = file_chapter_verses[verse]

                # Convert verse into JSON  Spacy Break down
                spacy_verse = getSpacyVerse(parsed_versed, verse_index_count)

                verse_list.append(
                    Verse(verse_number=verse_number, verse_string=spacy_verse, chapter_id=parsed_db_chapter_id))
                verse_index_count += 1

    print(datetime.datetime.now())

    return verse_list


def find_db_chapter_from_parse(db_chapters, file_chapter):
    for db_chapter in db_chapters:
        if file_chapter == db_chapter.chapter:
            return db_chapter.id


def run_command():
    # 2Qepxniw-setup-database
    command = input("Command: ")

    if command == 'a':
        print("Setting Up Database NIV")
        setup_bible_db()


if __name__ == '__main__':
    run_command()
