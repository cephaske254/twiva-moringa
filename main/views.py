from django.shortcuts import render
from django.views import View
from utils.requests.categories import get_latest

# Create your views here.


class Home(View):
    def get(self, request, *args, **kwargs):
        categories = get_latest()
        activeCat = request.GET.get("category", categories[0].id)
        context = {
            "categories": categories,
            "activeCat": activeCat,
        }

        return render(request, "main/home.html", context=context)
