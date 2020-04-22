#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def welcome():
    """
    return the string Hello HBNB! to web page
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    return the string HBNB to web page
    """
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
