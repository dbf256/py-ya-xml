Description
------------------------
py-ya-xml - is a python client library for Yandex.XML search service (http://xml.yandex.ru) compatible with
Python2 and Python3.

Install
------------------------
pip install pyyaxml

Usage
------------------------
- Receive API token and register your IP at https://xml.yandex.ru/ 
- Import YaSearch class from search.py, create a new instance using your api user/key and start your search.
```python
from pyyaxml.search import YaSearch
y = YaSearch('my_login', 'my_api_key')
results = y.search('python', page=1)
for result in results.items:
    print result.url
```
Don't forget to review https://yandex.ru/legal/xml/. See example.py for working example.
- Result of the search function contains list of result items (SearchResultItem), number of pages, error (if available)
and 'found_human' string that you need to display at result page according to Yandex.XML licence.

See also
------------------------
- http://xml.yandex.ru/
- https://tech.yandex.ru/xml/
