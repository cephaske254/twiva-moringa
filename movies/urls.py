from django.urls import path

from . import views

urlpatterns = [
    path("<tmdb_id>/comments/", views.Comments.as_view(), name="comments"),
    path("<tmdb_id>/", views.MovieDetail.as_view(), name="movie"),
]
