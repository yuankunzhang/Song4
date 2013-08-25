# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

from ..blog.models import Post

bp = Blueprint('frontend', __name__)


@bp.route('/')
def index():

    posts = Post.query.public_posts()

    return render_template('frontend/index.html',
                           posts=posts)
