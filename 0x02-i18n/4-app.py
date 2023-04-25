#!/usr/bin/env python3
"""
Module for 4. Force locale with URL parameter task.
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
    """Method for get locale."""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def root_path():
    """Method for root route."""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(port=5000)
