class CategoryMini:
    def __init__(self, data: dict = {}) -> None:
        self.name = data.pop("name", None)
        self.id = data.pop("id", None)
