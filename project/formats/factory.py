# -*- coding: utf-8 -*-

from exceptions import FormatNotFound
from .markdown import MarkdownFormat


FORMATS_MAP = {
    u'markdown': MarkdownFormat
}


def get_format_class_by_name(name):
    name = name.lower()
    if name not in FORMATS_MAP.keys():
        raise FormatNotFound(name)

    cls = FORMATS_MAP[name]
    instance = cls()

    return instance
