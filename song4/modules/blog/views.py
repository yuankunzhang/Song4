# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, \
    request, jsonify

from song4.utils.helper import str2list
from .models import Post

bp = Blueprint('blog', __name__)


@bp.route('/editor')
def editor():

    return render_template('blog/editor.html')


@bp.route('/publish', methods=['GET', 'POST'])
def publish():
    if request.method == 'POST':
        post_id = request.form['post_id']
        content = request.form['content']
        tags = str2list(request.form['tags'])

        if not post_id:     # new post
            post = Post(content)
            post.create()
            post.add_tags(tags)
            post.publish()
        else:
            post = Post.query.get(post_id)
            post.update()
        return jsonify(status='ok');
    else:
        return 'Good'


@bp.route('/save', methods=['POST'])
def save():
    post_id = request.form['post_id']
    content = request.form['content']
    tags = str2list(request.form['tags'])

    if not post_id:
        post = Post(content)
        post.create()
        post.add_tags(tags)
    else:
        post = Post.query.get(post_id)
        post.update()

    return jsonify(status='ok')
