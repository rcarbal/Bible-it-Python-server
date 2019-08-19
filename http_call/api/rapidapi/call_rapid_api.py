import requests
from config.keys import get_keys


def get_definition(word):
    keys = get_keys()
    print(keys);
    url = "https://wordsapiv1.p.rapidapi.com/words/{}/definitions".format(word)

    headers = {
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key': "{}".format(keys['rapid_key'])
    }

    response = requests.request("GET", url, headers=headers)
    res_text = response.text
    return res_text
