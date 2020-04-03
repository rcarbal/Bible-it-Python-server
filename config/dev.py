import os


def get_dev_keys():
    print("Inside dev.py >> get_dev_keys()")
    keys = {
        'rapid_key': os.getenv('RAPID_KEY'),
        'mw_dict_key': os.getenv('MW_DICT_KEY'),
        'mw_thesaurus_key': os.getenv('MW_THESAURUS_KEY')
    }

    return keys
