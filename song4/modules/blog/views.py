# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

bp = Blueprint('blog', __name__)


@bp.route('/editor')
def editor():
    return render_template('blog/editor.html')
