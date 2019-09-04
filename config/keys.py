import os

from config.dev import get_dev_keys
from config.prod import get_prod_keys


def get_keys():
    print("Inside keys.py >> get_keys()")
    if 'HOME' in os.environ and os.environ['HOME'] == 'production':
        print("Found os.environ HOME returning home")
        keys = get_prod_keys()
        return "Heroku"

    else:
        print("Inside DEV machuin returning get_dev-keys()")
        keys = get_dev_keys()
        return keys
