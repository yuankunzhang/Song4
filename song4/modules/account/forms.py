# -*- coding: utf-8 -*-
from wtforms import Form, TextField, PasswordField
from wtforms.validators import Required, Email, EqualTo, Length


class SignInForm(Form):

    email = TextField(u'Email', [
        Required(),
        Email(),
    ], id=u'signin-email')

    password = PasswordField(u'Password', [
        Required(),
    ], id=u'signin-password')


class SignUpForm(Form):

    email = TextField(u'Email', [
        Required(),
        Email(),
    ], id=u'signup-email')

    password = PasswordField(u'Password', [
        Required(),
        Length(min=6),
    ], id=u'signup-password')

    password_confirm = PasswordField(u'Confirm Password', [
        Required(),
        EqualTo('password'),
    ], id=u'signup-password-confirm')
