# -*-n coding: utf-8 -*-
"""
    Model for post tag.
"""
from song4.ext import db


class Tag(db.Model):

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(100), unique=True, nullable=False)
    num = db.Column(db.Integer, default=1)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Tag %r>' % self.name

    @staticmethod
    def create_or_update(name):
        tag = Tag.query.filter_by(name=name).first()

        if tag is None:
            tag = Tag(name)
            db.session.add(tag)
        else:
            tag.num += 1

        db.session.commit()
        return tag


class PostTags(db.Model):

    __tablename__ = 'post_tags'

    post_id = db.Column(
        db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(
        db.Integer, db.ForeignKey('tags.id'), primary_key=True)

    post = db.relationship(
        'Post', backref=db.backref('post_tags', cascade='all, delete-orphan'))
    tag = db.relationship(
        'Tag', backref=db.backref('tag_posts', cascade='all, delete-orphan'))

    def __init__(self, tag, post=None):
        self.tag = tag
        self.post = post
