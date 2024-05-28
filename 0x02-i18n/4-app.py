#!/usr/bin/env python3
""" A basic Flask app """
from flask import (
    Flask,
    request,
    render_template
)
from flask_babel import Babel
from typing import Union


class Config:
    """ Config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """ determine the best match with our supported languages """
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ Renders 2-index.html page """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
