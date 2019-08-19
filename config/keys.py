import os

from config.dev import get_dev_keys


def get_keys():
    print("Inside keys.py >> get_keys()")
    if 'HOME' in os.environ:
        print("HOME found")
        if os.environ['HOME'] == 'production':
            print("Found os.environ HOME returning home")
            return "Heroku"

    else:
        print("Inside DEV machuin returning get_dev-keys()")
        keys = get_dev_keys()
        return keys
