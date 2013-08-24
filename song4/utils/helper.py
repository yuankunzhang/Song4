# -*- coding: utf-8 -*-
"""
    Helper functions.
"""


def str2list(valuelist, seperator=',', remove_duplicates=True):
    """Convert a string into a value list"""

    values = []

    if valuelist:
        values = [x.strip() for x in valuelist.split(seperator)]

    if remove_duplicates:
        values = list(_remove_duplicates(values))

    return values


def _remove_duplicates(seq):

    d = {}

    for item in seq:
        if item.lower() not in d:
            d[item.lower()] = True
            yield item
