from pathlib import Path


def get_project_root() -> Path:
    """Returns project root folder."""
    return Path(__file__).parent.parent


def ordered_verses_by_book(verses):
    ordered_verses =[]

    x = range(1, 68)
    for n in x:
        for verse in verses:
            if n == verse.chapter.book_id:
                ordered_verses.append(verse)
    i = verses.count()
    ii = len(ordered_verses)
    return ordered_verses
