#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
    """
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return “Hello HBNB!”


