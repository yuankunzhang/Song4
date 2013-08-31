# -*- coding: utf-8 -*-
import os

_basedir = os.path.abspath(os.path.dirname(__file__))


class DefaultConfig(object):

    DEBUG = True

    ADMINS = frozenset(['feber007@gmail.com'])
    SECRET_KEY = 'Song for us'

    SQLALCHEMY_DATABASE_URI = 'mysql://root:900307@localhost/song4'
    SQLALCHEMY_ECHO = False


class ProductionConfig(object):

    DEBUG = False

    # path of log files
    DEBUG_LOG = os.path.join(_basedir, 'logs/debug.log')
    WARNING_LOG = os.path.join(_basedir, 'logs/warning.log')
    ERROR_LOG = os.path.join(_basedir, 'logs/error.log')

    SQLALCHEMY_DATABASE_URI = 'mysql://root:900307@127.0.0.1/song4-new'
    SQLALCHEMY_ECHO = False

class TestConfig(object):

    TESTING = True
