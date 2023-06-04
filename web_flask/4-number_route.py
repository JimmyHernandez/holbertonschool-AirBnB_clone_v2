#!/usr/bin/python3
"""
Script that starts a Flask application.
"""
from flask import Flask
from flask import abort


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_holberton():
    """
    Returns 'Hello HBNB!'.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display():
    """ Return display "HBNB" """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """ Display C and change _ to spaces"""
    txt = text.replace("_", " ")
    return "C " + txt


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """ Display Python"""
    txt = text.replace("_", " ")
    return "Python " + txt


@app.route("/number/<int:n>", strict_slashes=False)
def numbers(n):
    """ display n is a number"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
