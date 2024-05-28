#!/usr/bin/env python3
""" A basic Flask app """
from flask import (
    Flask,
    request,
    render_template,
    g
)
from flask_babel import Babel
from typing import Union
from os import getenv


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ Config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """ determine the best match with our supported languages """
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    elif g.user and g.user.get('locale')\
            and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[dict, None]:
    """ Returns user dict if ID can be found """
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        if user in users:
            return users.get(user)
    else:
        return None


@app.before_request
def before_request():
    """ Finds user and sets as global on flask.g.user """
    g.user = get_user()


@app.route('/')
def index():
    """ Renders 2-index.html page """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
