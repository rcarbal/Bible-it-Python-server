import json


# Reads data from json file found in /bible-json

def get_complete_bible():
    with open('bible-json/NIV.json') as json_file:
        data = json.load(json_file)
        return data


def get_all_bible_books(complete_bible_data):
    books = []
    for book in complete_bible_data.keys():
        books.append(book)

    return books


def get_book_from_bible(complete_bible_data, book):
    single_book = {}
    bible_book = complete_bible_data.get(book)
    single_book.update({book: bible_book})
    return bible_book


def get_verses_from_book(book):
    pass