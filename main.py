#!/usr/bin/env python3
import os

from database.database_utils import build_dictionary_verse_query, build_dictionary_book_query
from flask import Flask, request, render_template, Markup
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database.db_setup_niv import Verse, Book
from http_call.api.rapidapi.call_rapid_api import get_definition
from utilities.word_process import remove_pos

app = Flask(__name__)

Base = declarative_base()

engine = create_engine('sqlite:///database/bibledatabase.db?check_same_thread=False', echo=False)

Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/word_search', methods=['GET', 'POST'])
def search():
    query_param = None

    if request.method == 'POST':

        if 'word' in request.form:
            query_param = request.form['word']
        elif 'word' in request.args:
            query_param = request.args['word']

        verses = session.query(Verse).filter(Verse.verse_string.ilike('%' + query_param + '%'))

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
                                                                    '#exampleModalLong"' + '>' + word + '</a> '
                                                                    + '</strong>')
                    new_words = Markup(complete_words)
                    completed_dictionary['verse_string'] = new_words
                    completed_dictionary['index'] = index
                    exact.append(completed_dictionary)
                    pos_exact.append(first_pos)

        # Process Inexact results
        second_verses = session.query(Verse).filter(Verse.verse_string.like('%' + query_param + '%'))

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
            remove_first_separator, pos = remove_pos(exact_verse.verse_string, query_param)
            split_verse_into_words = remove_first_separator.split()

            second_slipt_into_words = []

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
                        match = False
                        original_word = original_word.replace(original_word, '<strong>' + '<a href="#">' + original_word
                                                              + '</a>' + '</strong>')

                second_slipt_into_words.append(original_word)

            if not match:
                index += 1
                joinned_verse = " ".join(second_slipt_into_words)
                markup_verse = Markup(joinned_verse)
                completed_dictionary['verse_string'] = markup_verse
                completed_dictionary['index'] = index
                second_exact.append(completed_dictionary)

        return render_template('word_search_result.html', verses=exact, pos_exact=pos_exact, second_verses=second_exact, count=len(exact),
                               word=query_param, second_count=len(second_exact))
    else:
        return render_template('search_word.html')


@app.route('/api/word/definition', methods=['GET'])
def word_definition():
    query_param = None
    if request.method == 'GET':

        if 'word' in request.args:
            query_param = request.args['word']

    definition = get_definition(query_param)

    return definition


if __name__ == '__main__':
    print("Bible-it Server Started ==================================================>")
    app.secret_key = 'super_secret_key'
    # port = int(os.environ.get('PORT', 8000))
    host = '127.0.0.1'
    app.debug = True
    # app.run(host='0.0.0.0')
    app.run(host=host, port=5000)
