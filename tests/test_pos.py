import spacy
import pdb

nlp = spacy.load('en_core_web_sm')

STRING = 'Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters'

doc = nlp(u"{}".format(STRING))
for token in doc:
    print("Text: {} , POS: {}".format(token.text, token.pos_))