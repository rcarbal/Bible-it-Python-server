def remove_pos(verse, word_search, second_parse=None):
    split_complete_string = verse.split("*")
    pos = ""

    # remove POS

    collected_verse_items = []

    for i in split_complete_string:
        pos_word_split = i.split("__")

        if "." in pos_word_split[0] \
                or "," in pos_word_split[0] \
                or "?" in pos_word_split[0] \
                or "!" in pos_word_split[0] \
                or ";" in pos_word_split[0]:
            pos_word_split[0] = pos_word_split[0].replace(" ", "")

        # Get word search POS
        compare = pos_word_split[0]
        if second_parse:
            if word_search.strip() in compare.strip():
                pos = pos_word_split[1]
        else:
            if word_search.strip() == compare.strip():
                if word_search == "":
                    pos = ""
                else:
                    pos = pos_word_split[1]

        collected_verse_items.append(pos_word_split[0])
    joined_complete = "".join(collected_verse_items)

    return joined_complete, pos


def retrieve_all_pos_in_verse(verse):
    pos = []

    split_complete_string = verse.split("*")
    for i in split_complete_string:
        pos_word_split = i.split("__")

        if len(pos_word_split) > 1:
            pos.append(pos_word_split[1])

    return pos
