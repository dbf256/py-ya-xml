# -*- coding: utf-8 -*-

from pyyaxml.search import YaSearch

# Put your Yandex.XML credentials here 
API_USER = ''
API_KEY = ''

y = YaSearch(API_USER, API_KEY)
results = y.search('питон', site='python.su', page=1)
if results.error is None:
    for result in results.items:
        print(result.url + ' ' + result.snippet)
else:
    print(results.error.code + ' ' + results.error.description)
  