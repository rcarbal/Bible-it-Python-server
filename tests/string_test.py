import spacy

nlp = spacy.load('en_core_web_sm')

verse = "When Jephthah returned to his home in Mizpah, who should come out to meet him but his daughter, dancing to the sound of tambourines! She was an only child. Except for her he had neither son nor daughter."
# split = verse.split()
# split_arr = ""
# print(split)

# for word in split:
#     # print(word)
#
#     word += '__{}'.format("NOUN")
#
#     split_arr += " " + word
#
# print(split_arr)

string_pos = ""

doc = nlp(u"{}".format(verse))
for token in doc:
    word_hold = ""

    word_hold += "{}__{}* ".format(token.text, token.pos_)

    string_pos += word_hold

print("\n\n\n\n\n Processing Verse to NLP\n")

print(string_pos)

print("\n\n Processing NLP string\n")
# undo string_pos

split_complete_string = string_pos.split("*")
print(split_complete_string)

print("\n\n Removing POS \n\n")
# remove POS

collected_verse_items = []

for i in split_complete_string:
    pos_word_split = i.split("__")
    print(pos_word_split)

    if "." in pos_word_split[0] or "," in pos_word_split[0] or "?" in pos_word_split[0] or "!" in pos_word_split[0]:
        print('\n\n"." has been found')
        pos_word_split[0] = pos_word_split[0].replace(" ", "")

    collected_verse_items.append(pos_word_split[0])

print("\n Extracted verse list \n")
print(collected_verse_items)

print("\n\n Joined Verse")
joined_complete = "".join(collected_verse_items)
print(joined_complete)
