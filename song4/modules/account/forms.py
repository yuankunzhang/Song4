# -*- coding: utf-8 -*-
from wtforms import Form, TextField, PasswordField
from wtforms.validators import Required, Email, EqualTo, Length


class SignUpForm(Form):

    email = TextField(u'Email', [
        Required(),
        Email(),
    ], id=u'signin-email')

    password = PasswordField(u'Password', [
        Required(),
        Length(min=6),
    ], id=u'signin-password')

    password_confirm = PasswordField(u'Confirm Password', [
        Required(),
        EqualTo('password'),
    ], id=u'signin-password-confirm')
