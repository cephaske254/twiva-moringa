from dataclasses import replace
from urllib.parse import urlencode, urljoin

import requests

base_url = "https://api.themoviedb.org/3/"
org_url = "https://themoviedb.org/"
image_base_url = urljoin(org_url, "t/p/")


def build_image_url(url: str, w: str = "w500") -> str:
    _url = url.replace("/", "", 1) if url.startswith("/") else url
    url_string = urljoin(image_base_url, "%s/%s" % (w, url))

    return url_string


class _Session(requests.Session):
    def request(self, method, url, **kwargs):

        api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ZjY3NTQ4NzgzZWViYzA0YWM5NzY5ZDYxNzY4NTA3MSIsInN1YiI6IjVlYTAwZDU5YmU0YjM2MDAxYzU4ZTVlZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.l1IrV4PcLQDkKHqWLWSJU1HsrY_om_SPW8uMTxIK2HY"
        self.params = urlencode({"api_key": api_key, **kwargs.pop("params", {})})

        self.headers.setdefault("Content-Type", "application/json")
        self.headers.setdefault("Authorization", "Bearer %s" % api_key)

        __url = urljoin(
            base_url,
            url,
        )

        modified_url = __url

        session = super(_Session, self).request(
            method, modified_url, headers=self.headers, params=self.params, **kwargs
        )
        return session


tmdb = _Session()
