# -*- coding: utf-8 -*-


class FormatNotFound(Exception):
    """
    Raised when an attempt to get a format fail because it wasn't found
    """
    def __init__(self, format_name, *args, **kwargs):
        super(FormatNotFound, self).__init__(format_name, *args, **kwargs)
        self.format_name = format_name
        self.message = u'Format {} Not Found. Make sure the format exists and \
            is listed in \'formats.factory.FORMATS_MAP\''.format(format_name)
