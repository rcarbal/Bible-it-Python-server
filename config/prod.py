import os


def get_dev_keys():
    print("Inside Production")
    keys = {
        'rapid_key': os.environ['RAPID_KEY'],
        'mw_dict_key': os.environ['MW_DICT_KEY'],
        'mw_thesaurus_key': os.environ['MW_THESAURUS_KEY']
    }