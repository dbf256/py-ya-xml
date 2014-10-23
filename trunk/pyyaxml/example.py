# -*- coding: utf-8 -*-
import sys

from pyyaxml.search import YaSearch


# Put your Yandex.XML credentials here 
API_USER = ''
API_KEY = ''

reload(sys)
sys.setdefaultencoding('utf8')
y = YaSearch(API_USER, API_KEY)
results = y.search(u'питон', site='python.su', page=1)
if results.error is None:
    for result in results.items:
        print result.url.encode('utf-8') + ' ' + result.snippet.encode('utf-8')
else:
    print unicode(results.error.code) + ' ' + results.error.description.encode('utf-8')
  