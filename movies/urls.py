from django.urls import path

from . import views

urlpatterns = [
    path("<tmdb_id>/", views.Comments.as_view()),
]
