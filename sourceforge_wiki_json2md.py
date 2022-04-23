#!/usr/bin/env python
# -*- coding: us-ascii -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
#
"""See sourceforge_wiki_download.py

Go through flat directory of json files that are in the format that sourceforge exports, sample schema:

    {
        "related_artifacts": [], 
        "attachments": [], 
        "title": "Home", 
        "text": "Markdown text in Windows newline format", 
        "labels": [], 
        "discussion_thread": {
            "posts": [], 
            "limit": 10, 
            "discussion_id": "??", 
            "_id": "???", 
            "page": null, 
            "subject": ""
        }, 
        "mod_date": "2017-04-10 16:06:15.799000", 
        "_id": """""", 
        "discussion_thread_url": "https://sourceforge.net/rest/p......"
    }
"""

import glob
import json
import os
import sys

filename_list = glob.glob('*.json')
for filename in filename_list:
    print(filename)
    f = open(filename, 'rb')
    data = json.load(f)
    f.close()
    if data['attachments']:
        raise NotImplemented('attachments support')
    fout = open(data['title'] + '.md', 'wb')
    fout.write(data['text'].encode('utf8'))
    fout.close()
