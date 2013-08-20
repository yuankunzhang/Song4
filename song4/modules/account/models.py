# -*- coding: utf-8 -*-
import datetime

from werkzeug import generate_password_hash, check_password_hash
from flask.ext.sqlalchemy import BaseQuery

from song4.ext import db, login_manager


class UserQuery(BaseQuery):
    """
    The Query class for User
    """

    def get_by_email(self, email):
        return self.filter_by(email=email).first()


class User(db.Model):
    """
    The User Model.
    """

    __tablename__ = 'users'
    query_class =UserQuery

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Unicode(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<User(email:%r)>' % (self.email)

    def _check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        user = User.query.get_by_email(self.email)
        if user is not None:
            raise Exception('This email address has been signed up.')
        else:
            self.password = generate_password_hash(self.password)
            db.session.add(self)
            db.session.commit()

    @classmethod
    def authenticate(cls, email, password):
        user = cls.query.get_by_email(email=email)
        if user:
            auth = user._check_password(password)
        else:
            auth = False

        return user, auth

    # Methods required by Flask-Login
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)
    # End


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(user_id)
