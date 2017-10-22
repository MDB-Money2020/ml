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
        return MenuItem(menu_item_dict['_key'], menu_item_dict['title'], menu_item_dict['category'],
                        menu_item_dict['description'], menu_item_dict['imageUrl'], menu_item_dict['price'],
                        menu_item_dict['restaurantId'], menu_item_dict['carbs'], menu_item_dict['protein'],
                        menu_item_dict['fat'], menu_item_dict['calories'], menu_item_dict['ingredients'])


class Stats:
    def __init__(self, calories_mean, calories_variance, carbs_mean, carbs_variance, fat_mean, fat_variance,
                 price_mean, price_variance, protein_mean, protein_variance, total_items):
        self.calories_mean = calories_mean
        self.calories_variance = calories_variance
        self.carbs_mean = carbs_mean
        self.carbs_variance = carbs_variance
        self.fat_mean = fat_mean
        self.fat_variance = fat_variance
        self.price_mean = price_mean
        self.price_variance = price_variance
        self.protein_mean = protein_mean
        self.protein_variance = protein_variance
        self.total_items = total_items

    @classmethod
    def construct_from_dict(cls, stat_dict):
        der = lambda key: stat_dict[key]
        return Stats(der('caloriesMean'), der('caloriesVariance'), der('carbsMean'), der('carbsVariance'),
                     der('fatMean'), der('fatVariance'), der('priceMean'), der('priceVariance'), der('proteinMean'),
                     der('proteinVariance'), der('totalItems'))
