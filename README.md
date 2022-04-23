# py-sourceforge-wiki-export

Python script(s) to export/dump a wiki from Sourceforge.net

Turns out SourceForge have a really great API to accessing the wiki, inspired by the Perl project https://github.com/primordial-soup/sourceforge-wiki-export/blob/master/dump-sf-wiki-json

  * sourceforge_wiki_download.py - downloads json files, unprocessed
  * sourceforge_wiki_json2md.py - simple extract of text body and save as text files (uses extension .md)
