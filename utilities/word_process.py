
def remove_pos(verse):
    split_complete_string = verse.split("*")

    # remove POS

    collected_verse_items = []

    for i in split_complete_string:
        pos_word_split = i.split("__")
        print(pos_word_split)

        if "." in pos_word_split[0] \
                or "," in pos_word_split[0] \
                or "?" in pos_word_split[0] \
                or "!" in pos_word_split[0] \
                or ";" in pos_word_split[0]:
            print('\n\n"." has been found')
            pos_word_split[0] = pos_word_split[0].replace(" ", "")

        collected_verse_items.append(pos_word_split[0])
    joined_complete = "".join(collected_verse_items)

    return joined_complete
