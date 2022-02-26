from utils.requests.models.movies import PaginatedMovieObject
from utils.tmdb import tmdb


def getMovieByCategory(categoryId: str):
    url = "discover/movie"
    req = tmdb.get(url, params={"with_genres": categoryId} if categoryId else {}).json()

    return PaginatedMovieObject(req, "w200")
