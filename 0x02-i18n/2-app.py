#!/usr/bin/env python3
""" Configuring my flask app to handle locale translation """

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Configuring available languages in my app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def hello_world() -> str:
    """ Returns some text """
    return render_template('2-index.html')


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """ Select a language translation to use """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=False)
