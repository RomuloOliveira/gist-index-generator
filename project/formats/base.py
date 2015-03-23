# -*- coding: utf-8 -*-


class BaseFormat(object):
    """
    Abstract class responsible for tranforming gist data structures into any
    text/binary format.

    Child classes must implement all methods defined in this class.
    """

    def render(self, gist):
        """
        Return a string with rendered gist in desired format
        """
        raise NotImplementedError()

    def __unicode__(self):
        """
        Return the class unicode string representation
        """
        raise NotImplementedError()

    def __str__(self):
        return str(self.__unicode__())
