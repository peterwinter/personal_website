#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'peter winter'
SITENAME = 'Peter B Winter PhD'
SITEURL = ''

STATIC_PATHS = ['images', 'pdfs', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

ARTICLE_PATHS = ['blog']
PAGE_ORDER_BY = 'date'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
Links = ()

# Social widget
SOCIAL = (('email', 'peterwinteriii@gmail.com'),
    ('twitter', 'https://twitter.com/pwinty'),
    ('linkedin', 'https://br.linkedin.com/in/peter-winter'),
    ('github', 'https://github.com/peterwinter'))

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

BIO = "Data Scientist"
PROFILE_IMAGE = "avatar.jpg"

DISQUS_SITENAME = "peterbwinter"

PLUGINS = ['pelican_gist']
