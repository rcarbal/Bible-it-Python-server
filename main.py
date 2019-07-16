#!/usr/bin/env python3

from flask import Flask, request, render_template
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database.db_setup_niv import Verse

app = Flask(__name__)

Base = declarative_base()

engine = create_engine('sqlite:///database/bibledatabase.db?check_same_thread=False')

Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def root():
    return "root"


@app.route('/word_search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query_param = request.form['word']
        verses = session.query(Verse).all()

        arr = []

        for verse in verses:
            if query_param in verse.verse_string:
                arr.append(verse.verse_string)

        return render_template('word_search_result.html', verses=arr)

    else:
        return render_template('search_word.html')


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    port = 5000
    host = '127.0.0.1'
    app.debug = True
    # app.run(host='0.0.0.0', port=5000)
    app.run(host=host, port=port)
