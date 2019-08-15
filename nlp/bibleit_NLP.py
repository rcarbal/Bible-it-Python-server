import spacy
import pdb

nlp = spacy.load('en_core_web_sm')


def getSpacyDictionary(verse, count):
    print(count)

    nlp_verse = nlp_process_verse(verse)
    pass


def nlp_process_verse(verse):
    string_pos = ""

    doc = nlp(u"{}".format(verse))
    for token in doc:

        word_hold = ""

        word['word'] = token.text
        word['pos'] = token.pos_

        string_pos += ""

    return word