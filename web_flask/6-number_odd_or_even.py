#!/usr/bin/python3
'''
script starts a Flask web application, listening  on 0.0.0.0, \
port 5000 and Routes: /, /hbn, /c/<text> and python/<text>
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''
    Routes: / and returns string
    '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
    Routes: /hbnb and returns string
    '''
    return "HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''
    Routes: /c/<text> and returns string value
    '''
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    '''
    Routes: python/<text> and return steing value
    '''
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def int_number(n):
    '''
    Route: /number/<int:n> if n is integer
    '''
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def temp_number(n):
    '''
    Route: /number_template/<n> if n is integer
    '''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    '''
    Routes: /number_odd_or_even/<n> if n is integer
    and renders for odd number or even number
    '''
    odd_or_even = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html',
                           n=n, odd_or_even=odd_or_even)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
