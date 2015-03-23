# -*- coding: utf-8 -*-


import requests


def _get_user_url(username):
    """
    Return a gist url for a given user
    """
    url = u'https://api.github.com/users/{}/gists'.format(username)
    return url


def _retrieve_gist(url):
    """
    Fetch gist `url` and return a JSON of raw data
    """
    r = requests.get(url)

    if r.status_code != 200:
        # FIXME: Change to a better exception
        raise Exception(u'Invalid status code from github: {}'.format(
            r.status_code
        ))

    return r.json()


# TODO: Support exclude_fields
def _parse_gists(data, exclude_fields=None):
    """
    Return a list of dicts from a JSON-encoded gist list.
    """
    gist = []
    raw_fields = [
        u'url', u'description', u'comments', u'created_at',
        u'updated_at'
    ]

    #
    # TODO: forks and stars
    #

    for d in data:
        g = {}

        #
        # Get "easy" fields
        #
        for field in raw_fields:
            value = d.get(field)
            if value is not None:
                g[field] = value

        #
        # get filename and language, if exists
        #
        filename = None
        language = None

        files = d.get('files', {})
        if files.keys():
            filename = files.keys()[0]
            language = files.values()[0][u'language']
            g[u'filename'] = filename
            g[u'language'] = language

        gist.append(g)

    return gist


# TODO: Allow to pass url or username
def parse_gist(gist_username):
    """
    Retrieve and parse a gist for a given user
    """
    url = _get_user_url(gist_username)
    gist = {
        u'username': gist_username,
        u'url': u'https://gist.github.com/{}'.format(gist_username),
        u'gists': _parse_gists(_retrieve_gist(url)),
    }

    return gist
