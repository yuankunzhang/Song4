# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, \
    request, jsonify
from flask.ext.login import login_required

from song4.utils.helper import str2list
from .models import Post

bp = Blueprint('blog', __name__)


@bp.route('/editor/')
@login_required
def editor():

    return render_template('blog/editor.html')


@bp.route('/publish/', methods=['GET', 'POST'])
@login_required
def publish():
    if request.method == POST:
        post_id = request.form['post_id']
        content = request.form['content']
        tags = str2list(request.form['tags'])
        access = request.form['access']

        if not post_id:     # new post
            post = Post(content, access)
            post.create()
            post.add_tags(tags)
            post.publish()
        else:
            post = Post.query.get(post_id)
            post.update(content, access, tags)
            post.publish()
        return jsonify(status='ok');
    else:
        return render_template('blog/editor.html')


@bp.route('/save/', methods=['POST'])
@login_required
def save():
    post_id = request.form['post_id']
    content = request.form['content']
    tags = str2list(request.form['tags'])
    access = request.form['access']

    if not post_id:
        post = Post(content)
        post.create()
        post.add_tags(tags)
    else:
        post = Post.query.get(post_id)
        post.update(content, access, tags)

    return jsonify(status='ok', post_id=post.id)


@bp.route('/edit/<post_id>')
@login_required
def edit(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('blog/editor.html', post=post)


@bp.route('/<post_id>/', methods=['GET'])
def entry(post_id):
    post = Post.query.get_or_404(post_id)

    return render_template('blog/entry.html', post=post)
