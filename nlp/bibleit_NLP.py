import spacy

nlp = spacy.load('en_core_web_sm')

def getSpacyDictionary(verse, count):
    print(count)
    
    pass

def process_verse(verse, verse_word):
    word = {}
    doc = nlp(u"{}".format(verse))
    for token in doc:

        if token.text == verse_word:
            word['word'] = verse_word
            word['pos'] = token.pos_

    return word
