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


@app.route('/c/<text>', strict_slashes=False)
def show_text_c(text):
    """
    return the string C append with <text> string.
    """
    str = text.replace('_', ' ')
    return 'C '+str


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python(text='is cool'):
    """
    return the string Python append with <text> string.
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
