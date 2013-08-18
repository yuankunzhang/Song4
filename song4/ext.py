# -*- coding: utf-8 -*-
"""
Extensions.
"""
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

__all__ = ['db', 'login_manager']

db = SQLAlchemy()
login_manager = LoginManager()
