# -*- coding: utf-8 -*-
import sys
from search import YaSearch

# Put your Yandex.XML credentials here 
API_USER = ''
API_KEY = ''

reload(sys)
sys.setdefaultencoding('utf8')
y = YaSearch(API_USER, API_KEY)
results = y.search(u'Guido', page=1, site='python.org')
if results.error is None:
    for result in results.items:
        print result.url + ' ' + result.snippet
else:
    print unicode(results.error.code) + ' ' + results.error.description
  