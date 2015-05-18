Description
------------------------
py-ya-xml - simple python wrapper for Yandex.XML search service (http://xml.yandex.ru)

Install
------------------------
pip install pyyaxml

Usage
------------------------
Import YaSearch class from search.py, create new instance using your api user/key and start your search.
Don't forget to review http://xml.yandex.ru/licence.xml.
See example.py for working example. Now you can pass host parameter to search function to search inside one (your)
website.
Result of the search function contains list of result items (SearchResultItem), number of pages, error (if available)
and 'found_human' string that you need to display at result page according to Yandex.XML licence.

See also
------------------------
http://xml.yandex.ru/
