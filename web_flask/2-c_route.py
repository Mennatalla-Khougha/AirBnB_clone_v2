#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello():
    """ display “Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ display “HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_is_fun(text):
    """ display “C ” followed by the value of the text variable"""
    txt = text.replace("_", " ")
    return f"C {txt}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
