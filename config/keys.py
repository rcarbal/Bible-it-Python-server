import os

from config.dev import get_dev_keys


def get_keys():
    if 'HOME' in os.environ:
        if os.environ['HOME'] == 'production':
            return "Heroku"

    else:
        return get_dev_keys()
