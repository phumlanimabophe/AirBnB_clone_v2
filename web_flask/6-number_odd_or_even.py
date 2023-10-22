#!/usr/bin/python3
"""
This script initializes a Flask web application with various routes.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """
    This route returns the message "Hello HBNB!"
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This route returns the message "HBNB"
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """
    This route displays "C " followed by the value of the 'text' variable
    """
    return 'C ' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """
    This route displays "Python ", followed by the value of the 'text' variable
    """
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """
    This route displays "n is a number" only if 'n' is an integer
    """
    return "{:d} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """
    This route displays an HTML page only if 'n' is an integer
    """
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
    """
    This route displays an HTML page only if 'n' is an integer and determines if it's odd or even
    """
    evenness = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, evenness=evenness)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
