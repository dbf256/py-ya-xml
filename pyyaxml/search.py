# -*- coding: utf-8 -*-
# Coded by Alexey Moskvin
from six.moves import urllib
from xml.dom import minidom
from six import PY2

class SearchResultItem:
    def __init__(self, url, title, snippet):
        self.url = url
        self.title = title
        self.snippet = snippet

class SearchResults:
    def __init__(self, items, pages, num_results, error=None):
        self.items = items
        self.pages = pages
        self.num_results = num_results
        self.error = error

class SearchError:
    def __init__(self, code, description):
        self.code = code
        self.description = description

class YaSearch:
    RESULTS_PER_PAGE = 10

    REQUEST_TEMPLATE = """<?xml version='1.0' encoding='utf-8'?>
        <request>
            <query>%s</query>
            <page>%s</page>
            <sortby order="%s" priority="no">%s</sortby>
            <maxpassages>0</maxpassages>
            <groupings>
		        <groupby mode="flat"/>
	        </groupings>
        </request>"""

    BASE_URL = u'https://yandex.{}/search/xml?'
    VALID_DOMAINS = {'ru', 'com.tr', 'com'}

    def _xml_extract_helper(self, node):
        result = ''
        for child in node.childNodes:
            if not len(child.childNodes):
                result += child.nodeValue
            else:
                result += child.childNodes[0].nodeValue
        return result

    def __init__(self, api_user, api_key, domain='ru'):
        self._api_user = api_user
        self._api_key = api_key
        if domain not in self.VALID_DOMAINS:
            raise ValueError('Invalid domain. Valid domains are {}'.format(', '.join(self.VALID_DOMAINS)))
        self._url = self.BASE_URL.format(domain)

    def _get_result_size(self, dom):
        for foundNode in dom.getElementsByTagName('found'):
            if foundNode.parentNode.nodeName == 'response':
                return int(foundNode.childNodes[0].nodeValue)
        return 0

    def _get_items(self, dom):
        items = []
        for docNode in dom.getElementsByTagName('doc'):
            (url, passage, title) = ('', '', '')
            for child in docNode.childNodes:
                if child.nodeName == 'url':
                    url = child.childNodes[0].nodeValue
                if child.nodeName == 'title':
                    title = self._xml_extract_helper(child)
                if child.nodeName == 'passages':
                    passage = self._xml_extract_helper(child.childNodes[0])
            items.append(SearchResultItem(url, title, passage))
        return items

    def _get_error(self, dom):
        error = None
        errorNodes = dom.getElementsByTagName('error')
        if len(errorNodes):
            description = errorNodes[0].childNodes[0].nodeValue
            try: # sometimes error code is not available in XML
                code = errorNodes[0].attributes['code'].value
            except Exception:
                code = 0
            error = SearchError(code, description)
        return error

    def _get_num_results(self, dom):
        if dom.getElementsByTagName('found') == []:
            num_results = 0
        else:
            num_results = int(dom.getElementsByTagName('found')[2].childNodes[0].nodeValue)
        return num_results

    """
    Call to search API. Check https://tech.yandex.ru/xml/doc/dg/concepts/response_request-docpage/ to see possible
    values.    
    """
    def search(self, query, page=1, site=None, max_page_num=100, sort_by='rlv', order='descending'):
        request_suffix = u''
        if site:
            request_suffix += (u' site:%s' % site)

        page -= 1
        params = {'user': self._api_user, 'key': self._api_key}
        query = query + request_suffix

        if PY2:
            search_url = self._url.encode('utf-8') + urllib.parse.urlencode(params)
            post_data = self.REQUEST_TEMPLATE % (query.encode('utf-8'), str(page), order.encode('utf-8'), sort_by.encode('utf-8'))
        else:
            search_url = self._url + urllib.parse.urlencode(params)
            post_data = (self.REQUEST_TEMPLATE % (query, str(page), order, sort_by)).encode('utf-8')

        req = urllib.request.Request(search_url, post_data)
        response = urllib.request.urlopen(req)
        xml = response.read()
        dom = minidom.parseString(xml)
        items = []
        pages = 0
        num_results = ''
        error = self._get_error(dom)
        if error is not None:
            search_results = SearchResults(items, pages, num_results, error)
            return search_results

        items = self._get_items(dom)
        result_size = self._get_result_size(dom)
        num_results = self._get_num_results(dom)

        pages = result_size / self.RESULTS_PER_PAGE
        if pages > max_page_num:
            pages = max_page_num

        search_results = SearchResults(items, pages, num_results)
        return search_results