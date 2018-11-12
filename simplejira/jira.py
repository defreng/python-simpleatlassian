import requests
import urllib.parse


class JIRA:
    def __init__(self, base_url, username=None, password=None, extra_headers=None, verify=True):
        self.jira_page_size = 50
        self.base_url = base_url

        self.session = requests.Session()

        if username is not None and password is not None:
            self.session.auth = (username, password)
        if extra_headers is not None:
            self.session.headers.update(extra_headers)
        self.session.verify = verify

    def _url(self, url):
        return urllib.parse.urljoin(self.base_url, url)

    def _request(self, method, url, *kargs, **kwargs):
        data = self.session.request(method, self._url(url), *kargs, **kwargs)
        return data.json()

    def get(self, url, *kargs, **kwargs):
        return self._request('GET', url, *kargs, **kwargs)

    def post(self, url, data, *kargs, **kwargs):
        return self._request('POST', url, *kargs, json=data, **kwargs)

    def put(self, url, data, *kargs, **kwargs):
        return self._request('PUT', url, *kargs, json=data, **kwargs)

    def post_files(self, url, files, *kargs, **kwargs):
        return self._request('POST', url, files=files, *kargs, **kwargs)

    def get_all(self, url, max=None, params=None, resultfield='values', *kargs, **kwargs):
        limit = self.jira_page_size
        offset = 0
        if params is None:
            params = {}

        while True:
            params.update({'maxResults': limit, 'startAt': offset})
            d = self.get(url, *kargs, params=params, **kwargs)

            if d is None:
                return

            for value in d[resultfield]:
                yield value
            offset += len(d[resultfield])

            if d.get('isLast', False) or offset >= d.get('total', 1e8) or (max is not None and offset >= max):
                return
