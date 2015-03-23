# -*- coding: utf-8 -*-

import os

from jinja2 import Environment, FileSystemLoader

from project.formats.base import BaseFormat


class MarkdownFormat(BaseFormat):
    def render(self, gist):
        """
        Return a string with rendered gist in desired format
        """
        template_path = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'templates'
        )

        env = Environment(
            loader=FileSystemLoader(template_path)
        )

        template = env.get_template(u'base.md')
        return template.render(**gist)

    def __unicode__(self):
        return u'Markdown'
