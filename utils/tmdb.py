from sys import api_version

import requests


class _RequestConfig:
    api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ZjY3NTQ4NzgzZWViYzA0YWM5NzY5ZDYxNzY4NTA3MSIsInN1YiI6IjVlYTAwZDU5YmU0YjM2MDAxYzU4ZTVlZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.l1IrV4PcLQDkKHqWLWSJU1HsrY_om_SPW8uMTxIK2HY"
    session: requests.Session

    def __init__(self) -> requests.Session:
        self.session = requests.Session()
        self.session.headers = {
            **self.session.headers,
            "Authorization": "Bearer %s" % self.api_key,
            "Content-Type": "application/json;charset=utf-8",
        }

        return self.session


tmdb = _RequestConfig()
