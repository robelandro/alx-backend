#!/usr/bin/env python3
"""
Module for 2. Get locale from request task.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Class for config."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Method to determine the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def root_path():
    """Method for root route."""
    return render_template("2-index.html")
