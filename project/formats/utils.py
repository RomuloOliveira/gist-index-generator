# -*- coding: utf-8 -*-

import factory

DEFAULT_FORMAT = u'markdown'


def get_default_format():
    return unicode(factory.get_format_class_by_name(DEFAULT_FORMAT))
