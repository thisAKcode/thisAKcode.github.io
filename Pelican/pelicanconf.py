#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Alex'
SITENAME = 'PrettyLagom'
SITEURL = ''
MARKUP = ("md", "ipynb")


from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup]
IPYNB_MARKUP_USE_FIRST_CELL = True

IGNORE_FILES = [".ipynb_checkpoints"]

STATIC_PATHS = ['images','extra/p5_stuff.html', 'extra/CNAME', 'html']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/p5_stuff.html': {'path': 'p5_stuff.html'},
                       'html/p5_stuff.html' : {'path' : 'p5_stuff.html'},}

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# ARTICLE_EXCLUDES = ['extra/p5_stuff.html']