from typing_extensions import Self
from django.contrib.auth import get_user_model
from django.db import models
from pyexpat import model
from django.db.models import QuerySet

# Create your models here.


class Movie(models.Model):
    tmdb_id = models.IntegerField(blank=False, null=False)

    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    @classmethod
    def get_or_create_object(cls, tmdb_id) -> QuerySet[Self]:
        try:
            return cls.objects.get(tmdb_id=tmdb_id)
        except:
            return cls.objects.create(tmdb_id=tmdb_id)


class Comment(models.Model):
    movie = models.ForeignKey(
        Movie, models.CASCADE, blank=False, null=False, related_name="comments"
    )
    user = models.ForeignKey(get_user_model(), models.CASCADE)
    comment = models.TextField(blank=False, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
