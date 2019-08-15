import spacy
import pdb


nlp = spacy.load('en_core_web_sm')


def getSpacyVerse(single_verse, count):
    # print(count)

    string_pos = ""

    doc = nlp(u"{}".format(single_verse))
    for token in doc:
        word_hold = ""

        word_hold += "{}__{}* ".format(token.text, token.pos_)

        string_pos += word_hold

    # print("\n\n\n\n\n Processing Verse to NLP\n")
    # print(string_pos)
    # print("\n")

    return string_pos


# needs to return a list of nlp processed verses
def nlp_process_verse(verse):
    string_pos = ""

    doc = nlp(u"{}".format(verse))
    for token in doc:
        word_hold = ""

        word_hold += "{}__{}* ".format(token.text, token.pos_)

        string_pos += word_hold

    print("\n\n\n\n\n Processing Verse to NLP\n")
    print(string_pos)
    print("\n")

    return string_pos

