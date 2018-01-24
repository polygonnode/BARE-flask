
from flask import Flask                     #import flask module
from app.views.home import home

def create_app():
    app = Flask(__name__)

    app.config.update(
        DEBUG = True,
        SECRET_KEY = 'secret_xxx'
    )

    app.register_blueprint(home)

    return app
