# -*- coding: utf-8 -*-

import unittest

from pyyaxml.search import YaSearch


class SearchTest(unittest.TestCase):

    # Try different combinations and check that no exceptions are thrown. Not an ideal test, but it is not easy to
    # validate results that depends on 3rd-party service and API key is required

    def test_search(self):
        y = YaSearch('', '', 'ru')
        y.search(u'python')
        y.search(u'питон')
        y.search(u'питон', page=1)
        y.search(u'питон', page=1, site='site.com')
        y.search(u'питон', page=1, site='site.com', max_page_num=5)
        y.search(u'питон', page=1, max_page_num=5, sort_by='tm', order='descending')
