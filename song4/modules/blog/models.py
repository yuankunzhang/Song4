# -*- coding: utf-8 -*-
import datetime

from flask.ext.sqlalchemy import BaseQuery

from song4.ext import db
from .consts import PostStatus, PostAccess


class PostQuery(BaseQuery):

    pass


class Post(db.Model):
    """
    The Post object.
    """

    __tablename__ = 'posts'
    query_class = PostQuery

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer,
                          db.ForeignKey('users.id'),
                          nullable=False)
    title = db.Column(db.UnicodeText)
    content = db.Column(db.UnicodeText)

    status = db.Column(db.SmallInteger, default=PostStatus.DRAFT)
    access = db.Column(db.SmallInteger, default=PostAccess.PUBLIC)

    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    date_published = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)

    author = db.relationship(
        'User', backref=db.backref('posts', cascade='all, delete-orphan'))

    def __init__(self, title, content, access):
        self.title = title
        self.content = content
        self.access = access

    def __repr__(self):
        return '<Post(%r)>' % self.title

    def create(self):
        """Create a new post in database"""
        self.date_created = datetime.datetime.utcnow()
        self.status = PostStatus.DRAFT
        db.session.add(self)
        db.session.commit()

    def update(self):
        """Edit an existing post"""
        self.date_modified = datetime.datetime.utcnow()
        # Do the changes.
        db.session.commit()

    def publish(self):
        """Make an existing post published"""
        self.date_published = datetime.datetime.utcnow()
        self.status = PostStatus.PUBLISHED
        db.session.commit()
