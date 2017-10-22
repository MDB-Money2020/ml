import numpy as np


def construct_feature_vector(menu_item):
    feature_vec = [menu_item.price, menu_item.carbs]
    feature_vec.append(menu_item.price)
    feature_vec.append(menu_item.carbs)
    feature_vec.append(menu_item.protein)
    feature_vec.append(menu_item.fat)
    feature_vec.append(menu_item.calories)
    return np.array(feature_vec)


def construct_feature_vectors(items):
    return [construct_feature_vector(item) for item in items]
