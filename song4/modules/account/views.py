# -*- coding: utf-8 -*-
from flask import Blueprint, request, redirect, \
    render_template, url_for
from flask.ext.login import login_user, login_required
from werkzeug import generate_password_hash

from song4.ext import db
from .models import User
from .forms import SignInForm, SignUpForm

bp = Blueprint('account', __name__)


@bp.route('/')
def index():

    return 'Account index page.'


@bp.route('/signin/', methods=['GET', 'POST'])
def signin():

    form = SignInForm(request.form)

    if request.method == 'POST' and form.validate():
        user, auth = User.authenticate(form.email.data,
                                       form.password.data)
        if auth:
            login_user(user)
            return redirect(url_for('frontend.index'))
        else:
            form.password.errors = (u'Wrong password',)

    return render_template('account/signin.html', form=form)


"""
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
"""


@bp.route('/signout/')
@login_required
def signout():

    pass
