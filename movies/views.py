from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from main.models import Comment, Movie
from utils.requests.movies import getMovie

# Create your views here.


class Comments(View):
    def post(self, request: HttpRequest, tmdb_id):
        movie = Movie.get_or_create_object(tmdb_id)
        _comment = request.POST.get("comment")

        comment = Comment(movie=movie, user=request.user, comment=_comment)
        comment.save()

        return JsonResponse(
            {
                "comment": comment.comment,
                "id": comment.id,
                "user": comment.user.username,
            }
        )

    def delete(self, request: HttpRequest, tmdb_id):
        comment = Comment.objects.filter(
            pk=request.GET.get("comment"),
            user=request.user,
            movie=Movie.get_or_create_object(tmdb_id),
        )
        comment.delete()
        return JsonResponse({"success": True})


class MovieDetail(View):
    def get(self, request: HttpRequest, tmdb_id: str):
        movie = Movie.get_or_create_object(tmdb_id)
        _comments = Comment.objects.filter(movie=movie) or []
        movie = getMovie(tmdb_id)
        comments = [
            (
                {
                    "comment": comment.comment,
                    "user": comment.user.username,
                    "id": comment.pk,
                }
            )
            for comment in _comments
        ]

        return render(
            request,
            "movies/movie.html",
            context={
                "movie": movie,
                "comments": comments,
                "title": "%s | %s" % (movie.detail.title, movie.detail.tagline),
            },
        )
