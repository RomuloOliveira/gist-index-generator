#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from project import gist
from project.formats import factory, utils

DEFAULT_FORMAT = utils.get_default_format()


def _parse_args():
    parser = argparse.ArgumentParser(description=u'Generate a gist index')
    parser.add_argument(u'gist_username',
                        help=u'Gist username to generate index')
    parser.add_argument(u'-f', u'--format', dest=u'format',
                        default=DEFAULT_FORMAT,
                        help=u'Output format. Default: {}'.format(
                            DEFAULT_FORMAT
                        ))
    parser.add_argument(u'-o', u'--output', dest=u'output',
                        help=u'Output file')

    return parser.parse_args()


# TODO:
def _write_file(f, text):
    """
    Write "text" to file "f"
    """
    return text


def main():
    args = _parse_args()
    gist_username = args.gist_username

    gist_data = gist.get_gist(gist_username)
    format_cls = factory.get_format_class_by_name(args.format)
    rendered = format_cls.render(gist_data)

    if args.output:
        _write_file(args.output, rendered)
    else:
        print rendered

if __name__ == '__main__':
    main()
