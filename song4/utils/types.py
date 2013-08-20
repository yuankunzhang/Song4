# -*- coding: utf-8 -*-
"""
Define some base types.
from flask.ext.wtf import Form as BaseForm


class Form(BaseForm):

    filters = [lambda x: x.strip()]
"""

class Enum(object):

    def __init__(self, *seq, **name):
        items = dict(zip(seq, range(len(seq))), **name).items()
        self.__dict__.update(items)

    def from_int(self, int_val):
        pass
