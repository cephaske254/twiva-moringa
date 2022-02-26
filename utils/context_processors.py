from django.urls import reverse
from svg.templatetags import svg


def load_nav_items(request):
    nav_items: list = [
        {
            "title": "Home",
            "icon": svg.svg("home-outline"),
            "path": reverse("home"),
        },
        {
            "title": "Discover",
            "icon": svg.svg("compass-outline"),
            "path": reverse("home") + "sss",
        },
        {
            "title": "Community",
            "icon": svg.svg("shopping-cart-outline"),
            "path": reverse("home") + "as",
        },
    ]

    return {"nav_items": nav_items, "top_bar_height": "70px"}
