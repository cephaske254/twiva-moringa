def load_nav_items(request):
    nav_items: list = [
        {"title": "Some title"},
        {"title": "Something again"},
        {"title": "Some title"},
    ]

    return {"nav_items": nav_items}
