#!/usr/bin/env python3
"""
Mock user login system with Flask-Babel.

This module demonstrates:

- Mocking user login using URL parameter ?login_as=[id].
- Setting g.user in before_request.
- Displaying localized messages for logged-in or anonymous users.
- Using the _() function for translations.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

# Mock users table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Flask-Babel configuration"""
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


babel = Babel(app, locale_selector=get_locale)
app.jinja_env.globals['get_locale'] = get_locale  # Template access


def get_user():
    """
    Get user dictionary based on login_as URL parameter.

    Returns:
        dict or None: User dictionary or None if not found.
    """
    try:
        user_id = int(request.args.get("login_as"))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Executed before each request; sets g.user"""
    g.user = get_user()


@app.route("/", strict_slashes=False)
def home():
    """
    Render the home page with localized messages.

    Returns:
        str: Rendered HTML page.
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
