import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from nlp.bibleit_NLP import getSpacyVerse
from utilities.filereader_niv import get_complete_bible, get_all_bible_books, get_book_from_bible
from utilities.matcher import get_bible_period, get_civilization, match_books_to_section

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


class Civilization(Base):
    __tablename__ = 'civilizations'

    id = Column(Integer, primary_key=True)
    position = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    first_year = Column(Integer, ForeignKey('years.id'), nullable=False)
    last_year = Column(Integer, ForeignKey('years.id'), nullable=False)


engine = create_engine('sqlite:///database/bibledatabase.db?check_same_thread=False', echo=False)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def setup_bible_db():
    add_years_to_db()
    setup_db_bible_general_periods()
    add_bible_sections_to_db()
    add_books_to_db()
    add_chapters_to_db()
    add_verses_to_db()


# methods to setup database
def add_years_to_db():
    print("Initiate Save Years to database")
    # get all the years
    all_years = []
    bible_period = get_bible_period()

    general_biblical_periods = get_years_from_list(collection=bible_period)
    all_years.extend(general_biblical_periods)

    civilization = get_civilization()

    civilizations = get_years_from_list(collection=civilization)
    all_years.extend(civilizations)

    # remove duplicates
    no_duplicates = list(dict.fromkeys(all_years))

    # sort the years from oldest to newest
    sorted_years = sorted(no_duplicates, key=int, reverse=False)
    print(sorted_years)

    # save timeline data to database
    years_db_object = years_convert_to_db_object(sorted_years=sorted_years)
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
            civil_arr.append(Civilization(position=bp['position'],
                                          name=bp['name'],
                                          first_year=first_year_result.id,
                                          last_year=last_year_results.id))

    # save to database
    session.add_all(civil_arr)
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
