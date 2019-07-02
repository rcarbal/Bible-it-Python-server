#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return "root"


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    port = 5000
    host = '127.0.0.1'
    app.debug = True
    # app.run(host='0.0.0.0', port=5000)
    app.run(host=host, port=port)