from utils.requests.models.movies import MovieDetailObject, PaginatedMovieObject
from utils.tmdb import tmdb


def getMovieByCategory(categoryId: str):
    url = "discover/movie"
    req = tmdb.get(url, params={"with_genres": categoryId} if categoryId else {}).json()

    return PaginatedMovieObject(req, "w200")


def getMovie(movie_id: str):
    req = tmdb.get(
        "movie/%s" % movie_id, params={"append_to_response": "videos,images"}
    ).json()

    return MovieDetailObject(req)
