"""
Main application file
"""

# third-party imports
from flask import Flask

# local imports
from . import api
from .api import models
from .db import db
from flask_migrate import Migrate
# from .api.datadaemon import init_daemon

migrate = Migrate()


def create_app(config):
    app = Flask(__name__)
    # load configurations
    app.config.from_object(config)
    # app.config.from_object(config[config_name])
    # initialize app database
    db.init_app(app)
    # initialize api app
    api.init_app(app)
    migrate.init_app(app, db)
    # init_daemon()

    return app
