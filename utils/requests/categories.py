from utils.tmdb import tmdb


def get_latest(id=None):
    req = tmdb.get()
