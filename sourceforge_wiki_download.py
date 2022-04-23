#!/usr/bin/env python
# -*- coding: us-ascii -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
#
"""sourceforge_wiki_download.py - also see sourceforge_wiki_json2md.py
Based on Perl code in https://github.com/primordial-soup/sourceforge-wiki-export/blob/master/dump-sf-wiki-json
"""

import json
import os
import sys
import time
import urllib2


def get_json(url):
    f = urllib2.urlopen(url)
    buf = f.read()
    f.close()
    data_dict = json.loads(buf)
    return data_dict

sf_project_name = 'predef'  # FIXME project name (or argv processing) goes here
wiki_url = 'https://sourceforge.net/rest/p/' + sf_project_name + '/wiki'

url_dict = get_json(wiki_url)
print(url_dict['pages'])

for page in url_dict['pages']:
    page_url = wiki_url + '/' + page
    page_filename = page + '.json'
    print(page_url)
    print('\t' + page_filename)
    page_dict = get_json(page_url)
    fout = open(page_filename, 'wb')
    fout.write(json.dumps(page_dict, indent=4))
    fout.close()
