import os

from config.dev import get_dev_keys
from config.prod import get_prod_keys


def get_keys():
    print("Inside keys.py >> get_keys()")
    if 'BIBLE_HOME' in os.environ and os.environ['BIBLE_HOME'] == 'production':
        print("Found os.environ HOME returning home")
        keys = get_prod_keys()
        return keys

    else:
        print("Inside DEV machuin returning get_dev-keys()")
        keys = get_dev_keys()
        return keys
