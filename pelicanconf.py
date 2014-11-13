#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from sitestuff import *


SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

#specific
THEME = 'support/themes/modpbs3'
BOOTSTRAP_THEME = 'journal'
TWITTER_USERNAME="rahuldave"

TYPOGRIFY=True

# Social widget
#SOCIAL = True
SUMMARY_MAX_LENGTH = 50
DEFAULT_PAGINATION = 2
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'attr_list']
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
NEWEST_FIRST_ARCHIVES = True

USE_FOLDER_AS_CATEGORY=False
#MENU
DISPLAY_PAGES_ON_MENU=False
DISPLAY_CATEGORIES_ON_MENU=False

ARTICLEDIR='posts'
PAGEDIR='pages'
PAGE_EXCLUDES=['othermd']
ARTICLE_EXCLUDES=['pages','othermd']
#categiries: homework, lecture, lab, project

start = SITEURL
def do_menuitems(start):
    menuitems = [
          ('Blog', "%s/blog_index.html" % start ),
          ('LxPrior', "http://www.lxprior.com"),
          ('About', "%s/about.html" % start ),
          ]
    return menuitems
MENUITEMS = do_menuitems(start)

INTERLINKS = {
    'wikipedia_en': 'http://en.wikipedia.org/wiki/',
    'wikipedia_es': 'http://es.wikipedia.org/wiki/',
    'ddg': 'https://duckduckgo.com/?q='
}
PLUGIN_PATHS = ['support/plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.notebook', 'liquid_tags.include_code',
           'liquid_tags.include_md']

EXTRA_HEADER = open('support/notebook_header.html').read().decode('utf-8')

STATIC_PATHS=['static', 'code', 'notebooks', 'files', 'extra/CNAME']

#INDEX_SAVE_AS='index.html'
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

DIRECT_TEMPLATES = ('tags', 'categories', 'authors', 'archives', 'blog_index')
PAGINATED_DIRECT_TEMPLATES = ('tags', 'categories', 'authors', 'archives', 'blog_index')