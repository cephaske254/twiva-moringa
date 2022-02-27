from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import QuerySet
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from main.models import Comment, Movie
from utils.requests.movies import getMovie

# Create your views here.


class Comments(View):
    @login_required
    def post(self, request: HttpRequest):
        movie = self.get_or_create_object(tmdb_id)
        tmdb_id = request.data.get("tmdb_id")

        comment = Comment(
            movie=movie, user=self.request.user, comment=request.data.get("comment")
        )
        comment.save()

        comments = Comment.objects.filter(tmdb_id=tmdb_id)

        return serializers.serialize("json", comments)

    def get(self, request: HttpRequest, tmdb_id, *args, **kwargs):

        return JsonResponse([])

    def get_or_create_object(self, tmdb_id) -> QuerySet[Movie]:
        try:
            return Movie.objects.get(tmdb_id=tmdb_id)
        except:
            return Movie.objects.create(tmdb_id=tmdb_id)


class MovieDetail(View):
    def get(self, request: HttpRequest, tmdb_id: str):
        movie = getMovie(tmdb_id)

        return render(
            request,
            "movies/movie.html",
            context={
                "movie": movie,
                "title": "%s | %s" % (movie.detail.title, movie.detail.tagline),
            },
        )
