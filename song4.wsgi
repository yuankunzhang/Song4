# -*- coding: utf-8 -*-
import os
import sys
import site
import uwsgi

_basedir = os.path.join(os.path.dirname(__file__))

sys.stdin = sys.stdout
site.addsitedir(os.path.join(_basedir, 'venv/lib/python2.6/site-packages'))

activate_this = os.path.join(_basedir, 'venv/bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

if _basedir not in sys.path:
	sys.path.append(_basedir)

from song4 import create_app
from song4.config import ProductionConfig

application = create_app(ProductionConfig())
wsgi.applications = {'/':application}
