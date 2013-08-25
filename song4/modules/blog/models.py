# -*- coding: utf-8 -*-
import datetime

from flask.ext.sqlalchemy import BaseQuery
from flask.ext.login import current_user
from sqlalchemy.ext.associationproxy import association_proxy

from song4.ext import db
from .consts import PostStatus, PostAccess
from ..tag.models import Tag


class PostQuery(BaseQuery):

    def public_posts(self):
        return self.filter_by(status=PostStatus.PUBLISHED,
                              access=PostAccess.PUBLIC).\
            order_by(Post.date_published.desc())

    def drafts(self, author_id):
        return self.filter_by(status=PostStatus.DRAFT,
                              author_id=author_id)


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
    tags = association_proxy('post_tags', 'tag')

    def __init__(self, content, access=PostAccess.PUBLIC):
        heading_line = content.split('\n', 1)[0]
        self.title = heading_line[1:].strip()
        self.content = content[len(heading_line):].strip()
        self.access = access
        self.author_id = current_user.id

    def __repr__(self):
        return '<Post(%r)>' % self.title

    def create(self):
        """Create a new post in database"""
        self.date_created = datetime.datetime.utcnow()
        self.status = PostStatus.DRAFT

        db.session.add(self)
        db.session.commit()

    def update(self, content, access=PostAccess.PUBLIC, tag_names=None):
        """Edit an existing post"""
        self.date_modified = datetime.datetime.utcnow()

        heading_line = content.split('\n', 1)[0]
        self.title = heading_line[1:].strip()
        self.content = content[len(heading_line):].strip()
        self.access = access

        old_tags = [tag for tag in self.tags]
        old_tag_names = [tag.name for tag in self.tags]

        for tag in old_tags:
            if tag.name not in tag_names:
                self.tags.remove(tag)

        for name in tag_names:
            if name not in old_tag_names:
                self.tags.append(Tag.create_or_update(name))

        db.session.commit()

    def publish(self):
        """Make an existing post published"""
        self.date_published = datetime.datetime.utcnow()
        self.status = PostStatus.PUBLISHED
        db.session.commit()

    def add_tags(self, tag_names):
        for name in tag_names:
            tag = Tag.create_or_update(name)

            if tag not in self.tags:
                self.tags.append(tag)

        db.session.commit()
