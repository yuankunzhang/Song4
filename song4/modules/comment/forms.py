# -*- coding: utf-8 -*-
from wtforms import Form, TextField, PasswordField, \
    HiddenField
from wtforms.validators import Required, Email


class CommentForm(Form):

    author_name = TextField(u'Your name', [
        Required(),
    ], id=u'comment-author-name')

    author_email = TextField(u'Your email', [
        Required(),
        Email(),
    ], id=u'comment-author-email')

    author_url = TextField(u'Your website', [
    ], id=u'comment-author-url')

    content = TextField(u'Content', [
        Required(),
    ], id=u'comment-content')

    post_id = HiddenField()
    author_id = HiddenField()
    author_ip = HiddenField()
