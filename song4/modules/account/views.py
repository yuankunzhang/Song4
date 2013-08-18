# -*- coding: utf-8 -*-
from flask import Blueprint, request, redirect, \
    render_template, url_for
from werkzeug import generate_password_hash

from song4.ext import db
from .models import User
from .forms import SignUpForm

bp = Blueprint('account', __name__)


@bp.route('/')
def index():

    return 'Account index page.'


@bp.route('/signin/', methods=['GET', 'POST'])
def signin():

    pass


@bp.route('/signup/', methods=['GET', 'POST'])
def signup():

    form = SignUpForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User()
        form.populate_obj(user)
        user.save()
        return redirect(url_for('frontend.index'))
    else:
        return render_template('account/signup.html', form=form)


@bp.route('/signout/')
def signout():

    pass
