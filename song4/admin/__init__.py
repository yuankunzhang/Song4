# -*- coding: utf-8 -*-
import os.path as op

from flask.ext.login import current_user
from flask.ext.admin import Admin, AdminIndexView
from flask.ext.admin.contrib.fileadmin import FileAdmin

__all__ = ['admin']

class PermissionCheck(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated()

class PhotoAlbum(FileAdmin):
    def is_accessible(self):
        return current_user.is_authenticated()

admin = Admin(name='Song4', index_view=PermissionCheck())

path = op.join(op.dirname(op.dirname(__file__)), 'static/uploads')
admin.add_view(PhotoAlbum(path, '/static/uploads/', name='Upload files'))
