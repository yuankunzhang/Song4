# -*- coding: utf-8 -*-
"""
    Helper functions.
"""
import re

from unidecode import unidecode


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


def slugify(text, delim=u'-'):

    if text is None:
        return None

    re_punct = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
    re_boundary = re.compile(r'(?<=[^\w\s])(?=\w)(?=[^\w\s])')
    max_len = 20

    results = []
    text = text[:max_len]
    text = re.sub(re_boundary, ' ', text)

    for word in re_punct.split(text.lower()):
        if unidecode(word) != u'[?]':
            results.extend(unidecode(word.lower()).split())

    return unicode(delim.join(results))
