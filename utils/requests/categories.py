from typing import List
from urllib import request

from utils.requests.models.categories import CategoryMini
from utils.tmdb import tmdb


def get_latest() -> List[CategoryMini]:
    req = tmdb.get("genre/tv/list", params={"page": 1})
    genres = [{"name": "All", id: None}, *req.json().get("genres", [])]

    return [(CategoryMini(category)) for category in genres]


def getMovieByCategory(categoryId: str):
    url = "discover/movie"
    req = tmdb.get(url, params={"with_genres": categoryId} if categoryId else {})
    print(req.json())
