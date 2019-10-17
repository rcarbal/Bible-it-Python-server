#!/usr/bin/env python3
import json
import os

from flask import Flask, request, render_template, Markup
from sqlalchemy import create_engine, desc, asc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from bi_classes.biblecalendar import BibleCalendar
from database.database_utils import build_dictionary_verse_query, build_dictionary_book_query
from database.db_classes_niv import Verse, Chapter, Book, Years, GeneralBiblePeriods, HistoricalPeriods
from http_call.api.rapidapi.call_rapid_api import get_definition, get_synonym
from http_call.api.meeriam.mw_api import get_mw_definition, get_mw_synonym
from utilities.filereader_niv import get_complete_bible
from utilities.word_process import remove_pos

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

BIBLE_STRING = ""

app = Flask(__name__)

Base = declarative_base()

engine = create_engine('sqlite:///database/bibledatabase.db?check_same_thread=False', echo=False)

Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def root():
    print("On root")
    return render_template('search_word.html')


@app.route('/word_search')
def search():
    query_param = None

    if 'word' in request.form:
        query_param = request.form['word']
    elif 'word' in request.args:
        query_param = request.args['word']

    verses = session.query(Verse).filter(Verse.verse_string.ilike('%' + query_param + '%')). \
        join(Chapter).join(Book).order_by(Book.id.asc(), Chapter.chapter.asc(), Verse.verse_number.asc())

    exact = []
    pos_exact = []
    index = 0
    # loop through verses result
    for exact_verse in verses:

        # pass the verse through SpaCy NLP
        # nlp_verse = process_verse(exact_verse.verse_string, query_param)

        # get current available information -  verse string, verse number and chapter
        verse_dictionary = build_dictionary_verse_query(exact_verse)

        # get chapter information
        book = session.query(Book).get(verse_dictionary["book_id"])

        # get the book name (name) , section name (section.name)
        completed_dictionary = {**verse_dictionary, **build_dictionary_book_query(book)}

        # split the words in the verse using *
        # removes the pos from the string
        remove_first_separator, first_pos = remove_pos(exact_verse.verse_string, query_param)

        words = remove_first_separator.split()

        # loop through the words and check
        for i in words:
            word = i

            if "." in word:
                word = word.replace(".", "")
            if "," in word:
                word = word.replace(",", "")
            if '"' in word:
                word = word.replace('"', "")
            if ";" in word:
                word = word.replace(';', "")
            if "?" in word:
                word = word.replace('?', "")
            if word == query_param:
                index += 1
                complete_words = remove_first_separator.replace(word, '<strong>' +
                                                                '<a href="#" data-toggle="modal" data-target="'
                                                                '#exampleModalLong' + str(
                    index) + '"' + '>' + word + '</a> '
                                                                + '</strong>')
                new_words = Markup(complete_words)
                completed_dictionary['verse_string'] = new_words
                completed_dictionary['index'] = index
                completed_dictionary['pos'] = first_pos
                exact.append(completed_dictionary)
                pos_exact.append(first_pos)
                break

    # Process Inexact results
    second_verses = session.query(Verse).filter(Verse.verse_string.like('%' + query_param + '%')). \
        join(Chapter).join(Book).order_by(Book.id.asc(), Chapter.chapter.asc(), Verse.verse_number.asc())

    second_exact = []
    match = True

    index = 0
    # loops through all verses
    for exact_verse in second_verses:
        match = True

        # get current available information -  verse string, verse number and chapter
        verse_dictionary = build_dictionary_verse_query(exact_verse)

        # get chapter information
        book = session.query(Book).get(verse_dictionary["book_id"])

        # get the book name (name) , section name (section.name)
        completed_dictionary = {**verse_dictionary, **build_dictionary_book_query(book)}

        # splits the verses per word
        # removes the pos from the query param
        remove_first_separator, pos = remove_pos(exact_verse.verse_string, query_param, True)
        split_verse_into_words = remove_first_separator.split()

        second_slipt_into_words = []

        main_word = None

        for i in split_verse_into_words:

            original_word = i

            if query_param in i.lower():

                if "!" in i:
                    i = i.replace('!', "")
                if ".'" in i:
                    i = i.replace(".'", "")
                if ".'\"" in i:
                    i = i.replace(".'\"", "")
                if "." in i:
                    i = i.replace(".", "")
                if "," in i:
                    i = i.replace(",", "")
                if '"' in i:
                    i = i.replace('"', "")
                if ";" in i:
                    i = i.replace(';', "")
                if "?" in i:
                    i = i.replace('?', "")

                if i != query_param:
                    ind = index + 1
                    match = False
                    main_word = original_word
                    original_word = original_word.replace(original_word, '<strong>' + '<a href="#" '
                                                                                      'data-toggle="modal" '
                                                                                      'data-target=" '
                                                                                      '#exampleModalInexact' + str(ind)
                                                          + '"' + '> '
                                                          + original_word
                                                          + '</a>' + '</strong>')

            second_slipt_into_words.append(original_word)

        if not match:
            index += 1
            joinned_verse = " ".join(second_slipt_into_words)
            markup_verse = Markup(joinned_verse)
            completed_dictionary['verse_string'] = markup_verse
            completed_dictionary['index'] = index
            completed_dictionary['main_word'] = main_word
            completed_dictionary['pos'] = pos
            second_exact.append(completed_dictionary)
            continue

    return render_template('word_search_result.html', verses=exact, pos_exact=pos_exact, second_verses=second_exact,
                           count=len(exact),
                           word=query_param, second_count=len(second_exact))


@app.route('/timeline', methods=['GET'])
def timeline():
    # retrieve database years
    years = session.query(Years).all()

    # get years
    cal = BibleCalendar()
    converted_to_bible_dates = cal.convert_int_to_cal_year(int_dates_list=years)

    # get periods
    periods = session.query(GeneralBiblePeriods).all()

    years_and_periods = cal.append_bperiods_to_years(years=converted_to_bible_dates, bible_periods=periods)

    #
    return render_template('timeline.html', years=years_and_periods)


@app.route('/timelinetest', methods=['GET'])
def timeline_test():
    # get historical periods
    years = session.query(Years).all()

    # get historical period
    historical_periods = session.query(HistoricalPeriods).all()

    historical_period_list = []
    for h in historical_periods:
        first_year = session.query(Years).filter(Years.id == h.first_year_id).first().year
        last_year = session.query(Years).filter(Years.id == h.last_year_id).first().year
        # setup custom json for the timeline.js file
        period = {
            'name': h.name,
            'first_year': first_year,
            'last_year': last_year
        }
        historical_period_list.append(period)

    historical_json = json.dumps(historical_period_list)

    return render_template('timeline.html', years=years, main_history=historical_json)


@app.route('/api/word/definition', methods=['GET'])
def word_definition():
    query_param = None
    if request.method == 'GET':

        if 'word' in request.args:
            query_param = request.args['word']

    definition = get_mw_definition(query_param)

    return definition


@app.route('/api/word/synonym', methods=['GET'])
def word_synonym():
    query_param = None
    if request.method == 'GET':

        if 'word' in request.args:
            query_param = request.args['word']

    synonym = get_mw_synonym(query_param)
    bible = {"bible_string": BIBLE_STRING}
    synonym.insert(0, bible)

    complete = json.dumps(synonym)

    return complete


@app.route('/api/chapter', methods=['GET'])
def get_chapter():
    book = None
    chapter_id = None
    verse = None

    if request.method == 'GET':
        req_args = request.args
        if 'book' in req_args and 'chapter' in req_args and 'verse' in req_args:
            book = req_args['book']
            chapter_id = req_args['chapter']
            verse = req_args['verse']

        # retrieve the chapter from the database
        verses = session.query(Verse).filter_by(chapter_id=chapter_id). \
            join(Chapter).order_by(Verse.verse_number.asc())

        readable_verses = []

        for v in verses:
            # convert raw verse data to readable verses
            # get current available information -  verse string, verse number and chapter
            print(v.verse_number)
            remove_first_separator, first_pos = remove_pos(v.verse_string, "")

            readable_verses.append(remove_first_separator)
        json_string = json.dumps(readable_verses)
        return json_string


# On last test rapid api was not returning response
# API is on hold.
def rapid_api_word_definitions():
    query_param = None
    if request.method == 'GET':

        if 'word' in request.args:
            query_param = request.args['word']

    definition = get_definition(query_param)

    return definition


if __name__ == '__main__':
    print("Bible-it Server Started ==================================================>")
    BIBLE_STRING = get_complete_bible('./bible-json/NIV.json')
    app.secret_key = 'super_secret_key'
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
