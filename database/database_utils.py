def build_dictionary_verse_query(verse):
    verse_dictionary = {
        'verse_number': verse.verse_number,
        'chapter_number': verse.chapter.chapter,
        'book_id': verse.chapter.book_id
    }

    return verse_dictionary


def build_dictionary_book_query(book):
    book_dictionary = {
        'book_name': book.name,
        'section_name': book.section.name
    }
    return book_dictionary
