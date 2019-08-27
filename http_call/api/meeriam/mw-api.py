import requests
from config.keys import get_keys


def get_mw_definition(word="God"):
    keys = get_keys()

    url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/{}?key={}".format(word,
                                                                                              keys['mw_dict_key'])

    response = requests.request("GET", url)
    res_text = response.text
    return res_text

get_mw_definition()
