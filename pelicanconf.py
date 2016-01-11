#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'TakesxiSximada'
SITENAME = 'sximada.2016'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/TakesxiSximada'),
    ('Facebook', 'https://www.facebook.com/takesxi.sximada'),
    ('Github', 'https://github.com/TakesxiSximada'),
    ('BitBucket', 'https://bitbucket.org/takesxi_sximada'),
    ('about.me', 'https://about.me/TakesxiSximada'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


THEME = 'themes/pelican-twitchy'
STATIC_PATHS = ['static']

GOOGLE_ANALYTICS = 'UA-72260316-1'  # Tracking ID
