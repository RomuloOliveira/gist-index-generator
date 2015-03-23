# -*- coding: utf-8 -*-


from parser import parse_gist


def get_gist(gist_username):
    """
    Return a list of dicts representing a collection of gists.
    Fields:

        - username
        - url
        - gists
            - url
            - description
            - filename [optional]
            - language [optional]
            - created_at
            - updated_at
            - forks
            - stars
            - comments

    """
    return parse_gist(gist_username)
