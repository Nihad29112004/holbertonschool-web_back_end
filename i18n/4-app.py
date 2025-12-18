#!/usr/bin/env python3
"""
Force locale with URL parameter using Flask-Babel.

This module allows the user to force a locale via the URL
parameter ?locale=[en|fr]. It uses Flask-Babel for translations
and demonstrates the use of the _() gettext function.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _  # _() used for translations

class Config(object):
    """
    Configuration for Flask-Babel.

    Attributes:
        LANGUAGES (list): Supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)


def get_locale():
    """
    Determine the locale to use.

    Checks URL parameter ?locale=fr|en first.
    If not present or unsupported, returns best match from Accept-Language header.

    Returns:
        str: Locale code ('en' or 'fr').
    """
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


# Initialize Babel with locale_selector
babel = Babel(app, locale_selector=get_locale)
app.jinja_env.globals['get_locale'] = get_locale  # template use


@app.route("/", strict_slashes=False)
def home():
    """
    Render the home page with localized messages.

    Uses the _() function to translate strings in the template.

    Returns:
        str: Rendered HTML page.
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
