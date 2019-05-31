import json

def get_complete_bible():
    with open('../bible-json/NIV.json') as json_file:
        data = json.load(json_file)
        return data