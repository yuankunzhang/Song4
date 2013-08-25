# -*- coding: utf-8 -*-
import os
from song4 import create_app

_basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
activate_this = os.path.join(_basedir, 'venv/bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

app = create_app()
app.run(host='0.0.0.0')
