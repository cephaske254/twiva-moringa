from ctypes import Union
from urllib.parse import urljoin

from utils.tmdb import base_url, build_image_url


class MovieObject:
    def __init__(self, data, w: str = "w200") -> None:
        self.id: int = data.pop("id")
        self.poster_path: Union[str, None] = build_image_url(
            data.pop("poster_path"),
            w,
        )
        self.adult: bool = data.pop("adult")
        self.overview: str = data.pop("overview")
        self.release_date: str = data.pop("release_date")
        self.original_title: str = data.pop("original_title")
        self.original_language: str = data.pop("original_language")
        self.title: str = data.pop("title")
        self.backdrop_path: Union[str, None] = data.pop("backdrop_path")
        self.popularity: int = data.pop("popularity")
        self.vote_count: int = data.pop("vote_count")
        self.vote_average: int = data.pop("vote_average")
        self.video: bool = data.pop("video")


class PaginatedMovieObject:
    def __init__(self, data, w: str = None) -> None:
        self.total_pages = data.pop("total_pages")
        self.total_results = data.pop("total_results")
        self.results = [(MovieObject(res)) for res in data.pop("results", [])]
        self.page = data.pop("page")
