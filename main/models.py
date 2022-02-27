from django.contrib.auth import get_user_model
from django.db import models
from pyexpat import model

# Create your models here.


class Movie(models.Model):
    tmdb_id = models.IntegerField(blank=False, null=False)

    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    movie = models.ForeignKey(
        Movie, models.CASCADE, blank=False, null=False, related_name="comments"
    )
    user = models.ForeignKey(get_user_model(), models.CASCADE)
    comment = models.TextField(blank=False, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
