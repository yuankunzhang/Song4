# -*- coding: utf-8 -*-
import datetime

from song4.ext import db
from .consts import CommentStatus


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    author_name = db.Column(db.String(100))
    author_email = db.Column(db.String(120))
    author_url = db.Column(db.String(200))
    author_ip = db.Column(db.String(100))
    content = db.Column(db.UnicodeText)

    date_created = db.Column(db.DateTime, default=datetime.datetime.now)
    status = db.Column(db.SmallInteger, default=CommentStatus.APPROVED)
    parent_id = db.Column(db.Integer, db.ForeignKey('comments.id'))

    posts = db.relationship(
        'Post', backref=db.backref('comments', cascade='all, delete-orphan'))
    author = db.relationship(
        'User', backref=db.backref('comments', cascade='all, delete-orphan'))

    def __init__(self, content, post_id, author_name, author_email, **attr):
        self.content = content
        self.post_id = post_id
        self.author_name = author_name
        self.author_email = author_email
        self.__dict__.update(attr)

    def save(self):
        db.session.add(self)
        db.session.commit()
