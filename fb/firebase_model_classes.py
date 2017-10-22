class MenuItem:
    def __init__(self, menu_item_id, title, category, description, image_url, price, restaurant_id,
                 carbs, protein, fat, calories, ingredients):
        self.menu_item_id = menu_item_id
        self.title = title
        self.category = category
        self.description = description
        self.image_url = image_url
        self.price = price
        self.restaurant_id = restaurant_id
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
        self.calories = calories
        self.ingredients = ingredients

    @classmethod
    def construct_from_dict(cls, menu_item_dict):
        return MenuItem(menu_item_dict.menu_item_id, menu_item_dict.title, menu_item_dict.category,
                        menu_item_dict.description, menu_item_dict.image_url, menu_item_dict.price,
                        menu_item_dict.restaurant_id, menu_item_dict.carbs, menu_item_dict.protein,
                        menu_item_dict.fat, menu_item_dict.calories, menu_item_dict.ingredients)
