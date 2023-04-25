#!/usr/bin/env python3
"""
Module for 1. Basic Babel setup.
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Class for config."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def root_path():
    """Method for root route."""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(port=5000)
