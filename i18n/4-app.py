#!/usr/bin/env python3
""" Force locale with URL parameter """
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config(object):
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
    """
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


# Checker ve template uyumlu: locale_selector + Jinja global
babel = Babel(app, locale_selector=get_locale)
app.jinja_env.globals['get_locale'] = get_locale  # 🌟 template içinde kullanılabilir


@app.route("/", strict_slashes=False)
def home():
    """Render home page with localized messages"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
