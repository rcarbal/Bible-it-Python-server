import json


def get_complete_bible():
    with open('../bible-json/NIV.json') as json_file:
        data = json.load(json_file)
        return data

def get_all_bible_books(complete_bible_data):
    books = []
    for book in books.keys():
        books.append(book)

    return books


def get_book_from_bible(complete_bible_data, book):
    book = []
    bible_book = complete_bible_data[book]
    print(bible_book)


bible = get_complete_bible()
book = get_book_from_bible(bible, 'Genesis')
# print(book)