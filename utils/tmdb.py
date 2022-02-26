from urllib.parse import parse_qsl, urlencode, urljoin

import requests


class _Session(requests.Session):
    def request(self, method, url, **kwargs):

        api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ZjY3NTQ4NzgzZWViYzA0YWM5NzY5ZDYxNzY4NTA3MSIsInN1YiI6IjVlYTAwZDU5YmU0YjM2MDAxYzU4ZTVlZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.l1IrV4PcLQDkKHqWLWSJU1HsrY_om_SPW8uMTxIK2HY"
        self.params = urlencode({"api_key": api_key, **kwargs.pop("params", {})})

        self.headers.setdefault("Content-Type", "application/json")
        self.headers.setdefault("Authorization", "Bearer %s" % api_key)

        __url = urljoin(
            "https://api.themoviedb.org/3/",
            url,
        )

        modified_url = __url

        session = super(_Session, self).request(
            method, modified_url, headers=self.headers, params=self.params, **kwargs
        )
        return session


tmdb = _Session()
