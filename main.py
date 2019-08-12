#!/usr/bin/env python3
import os
from objects import verse
from typing import List

from flask import Flask, request, render_template, Markup
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database.db_setup_niv import Verse, Book

app = Flask(__name__)

Base = declarative_base()

engine = create_engine('sqlite:///database/bibledatabase.db?check_same_thread=False', echo=True)

Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/word_search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query_param = request.form['word']
        verses = session.query(Verse).filter(Verse.verse_string.ilike('%' + query_param + '%'))


        exact = []

        # loop through verses result
        for verse in verses:

            verse_dictionary = {}

            # get current available information -  verse string, verse number and chapter

            verse_dictionary['verse_string'] = verse.verse_string
            verse_dictionary['verse_number'] = verse.verse_number
            verse_dictionary['chapter_number'] = verse.chapter.chapter
            verse_dictionary['book_id'] = verse.chapter.book_id

            # get chapter information
            book = session.query(Book).get(verse_dictionary["book_id"])

            # get the book name (name) , section name (section.name)
            verse_dictionary['book_name'] = book.name
            verse_dictionary['section_name'] = book.section.name

            # split the words in the verse
            words = verse.verse_string.split()

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
                    complete_words = verse.verse_string.replace(word, '<strong>' + word + '</strong>')
                    new_words = Markup(complete_words)
                    exact.append(new_words)

        # Process Inexact results
        second_verses = session.query(Verse).filter(Verse.verse_string.like('%' + query_param + '%'))

        second_exact: List[str] = []
        match = True

        # loops through all verses
        for verse in second_verses:
            match = True
            # splits the verses per word
            split_verse_into_words = verse.verse_string.split()

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
                        original_word = original_word.replace(original_word, '<strong>' + original_word + '</strong>')

                second_slipt_into_words.append(original_word)

            if not match:
                joinned_verse = " ".join(second_slipt_into_words)
                markup_verse = Markup(joinned_verse)
                second_exact.append(markup_verse)

        return render_template('word_search_result.html', verses=exact, second_verses=second_exact, count=len(exact),
                               word=query_param, second_count=len(second_exact))
    else:
        return render_template('search_word.html')


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    port = int(os.environ.get('PORT', 8000))
    host = '127.0.0.1'
    app.debug = True
    # app.run(host='0.0.0.0', port=5000)
    app.run(host=host, port=port)
