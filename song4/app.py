# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from mongokit import Connection

from .config import DefaultConfig
from .ext import db, login_manager
from .modules import frontend, account, blog

__all__ = ['create_app']

APP_NAME = 'song4'

MODULES = (
    (frontend.bp, ''),
    (account.bp, '/u'),
    (blog.bp, '/blog'),
)


def create_app(config=None,
               app_name=APP_NAME,
               modules=MODULES):
    """Create the application instance."""

    app = Flask(app_name)

    config_app(app, config)
    config_ext(app)
    config_err(app)
    config_modules(app, modules)

    return app


def config_app(app, config):
    """Configure our application."""

    app.config.from_object(DefaultConfig())

    if config is not None:
        app.config.from_object(config)


def config_ext(app):
    """Configure extensions of our application."""

    db.init_app(app)
    login_manager.init_app(app)


def config_err(app):
    """Register handlers for visiting errors."""

    @app.errorhandler(404)
    def page_not_found(error):
        if request.is_xhr:
            return jsonify(error='404 page not found')
        return render_template('error.html', error=error)


def config_modules(app, modules):
    """Register visable modules."""

    for module, url_prefix in modules:
        app.register_blueprint(module, url_prefix=url_prefix)
