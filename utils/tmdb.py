import requests

tmdb = requests.Session()
_api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ZjY3NTQ4NzgzZWViYzA0YWM5NzY5ZDYxNzY4NTA3MSIsInN1YiI6IjVlYTAwZDU5YmU0YjM2MDAxYzU4ZTVlZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.l1IrV4PcLQDkKHqWLWSJU1HsrY_om_SPW8uMTxIK2HY"


tmdb.headers.update(
    {
        "Authorization": "Bearer %s" % _api_key,
        "Content-Type": "application/json;charset=utf-8",
    }
)
