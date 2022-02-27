from django.shortcuts import render
from django.views import View
from utils.requests.categories import get_latest
from utils.requests.movies import getMovieByCategory

# Create your views here.


class Home(View):
    def get(self, request, *args, **kwargs):
        categories = get_latest()
        activeCat = request.GET.get("category", categories[0].id)
        movies = getMovieByCategory(activeCat)

        context = {
            "categories": categories,
            "activeCat": activeCat,
            "movies": movies,
        }

        return render(request, "main/home.html", context=context)
