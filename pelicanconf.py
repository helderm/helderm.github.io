#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Helder Martins'
SITENAME = u'CHANGELOG'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

DEFAULT_METADATA = {
    'status': 'draft',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('GitHub', 'http://github.com/helderm'),
          ('LinkedIn', 'http://br.linkedin.com/in/helderm'),
          ('Facebook', 'https://www.facebook.com/heldergaray'),
          ('Twitter', 'https://twitter.com/heldergaray'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Themes Options (html5-dopetrope)
THEME = './themes/html5-dopetrope'
MAIL = 'heldergaray@gmail.com'
TWITTER_USER = 'heldergaray'
GOOGLEPLUS_USER = '108735776655822151608'
#LINKEDIN_USER = 'helderm'
FACEBOOK_USER = 'heldergaray'
ABOUT_TEXT = 'A place where I can ramble about technology and living abroad.'
ABOUT_IMAGE = 'theme/images/profile.jpg'
# ABOUT_LINK : Will add a link under the ABOUT_TEXT page
