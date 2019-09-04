import requests
from config.keys import get_keys
import json


def get_mw_definition(word):
    keys = get_keys()

    url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/{}?key={}".format(word,
                                                                                             keys['mw_dict_key'])

    response = requests.request("GET", url)
    res_text = response.text
    return res_text


def get_mw_synonym(word):
    keys = get_keys()

    url = "https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{}?key={}".format(word
                                                                                            ,keys['mw_thesaurus_key'])

    response = requests.request("GET", url)
    res_json = json.loads(response.text)
    return res_json
