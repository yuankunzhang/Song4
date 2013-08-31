# -*- coding: utf-8 -*-
import os

_basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
activate_this = os.path.join(_basedir, 'venv/bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

from flask import current_app
from flask.ext.script import Manager

from song4 import create_app
from song4.ext import db
from song4.config import ProductionConfig
from song4.modules.account.models import User
from song4.modules.blog.models import Post
from song4.modules.tag.models import Tag, PostTags

manager = Manager(create_app(ProductionConfig()))


@manager.shell
def make_shell_context():

    return dict(app=current_app)


@manager.command
def db_init():
    """Init the database. Use this method with caution."""

    db.drop_all()
    db.create_all()


@manager.command
def db_create_all():
    """Create all database tables"""

    db.create_all()


if __name__ == '__main__':
    manager.run()
