# -*- coding: utf-8 -*-
from flask import Blueprint

bp = Blueprint('comment', __name__)


@bp.route('/submit/', methods=['POST'])
def submit():
    """Submit a comment"""

    pass
