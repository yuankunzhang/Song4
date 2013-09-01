# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify
from flask.ext.login import current_user

from .models import Comment
from .forms import CommentForm

bp = Blueprint('comment', __name__)


@bp.route('/submit/', methods=['POST'])
def submit():
    """Submit a comment"""

    form = CommentForm(request.form)
    form.author_ip.data = request.remote_addr

    if current_user.is_authenticated():
        form.author_id.data = current_user.id
        form.author_name.data = current_user.username
        form.author_email.data = current_user.email
    elif not form.validate():
        return jsonify(status='err')

    comment = Comment()
    form.populate_obj(comment)
    comment.save()

    return jsonify(status='ok')
