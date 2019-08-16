import requests

from config.keys import get_keys

keys = get_keys()
print(keys)

url = "https://wordsapiv1.p.rapidapi.com/words/cow/definitions"

headers = {
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
    'x-rapidapi-key': "{}".format(keys['rapid_key'])
    }

response = requests.request("GET", url, headers=headers)

print(response.text)