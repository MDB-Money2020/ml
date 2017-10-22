import numpy as np
from math import sqrt
from fb.firebase_functions import get_global_stats


def construct_feature_vector(menu_item):
    feature_vec = []
    feature_vec.append(menu_item.price)
    feature_vec.append(menu_item.carbs)
    feature_vec.append(menu_item.protein)
    feature_vec.append(menu_item.fat)
    feature_vec.append(menu_item.calories)
    return np.array(feature_vec)


def construct_feature_vectors(items):
    return [construct_feature_vector(item) for item in items]


def normalize_demean(vectors):
    stats = get_global_stats()
    global_mean = [stats.price_mean, stats.carbs_mean, stats.protein_mean, stats.fat_mean, stats.calories_mean]
    global_variance = [stats.price_variance, stats.carbs_variance, stats.protein_variance, stats.fat_variance,
                       stats.calories_variance]
    for vector in vectors:
        for dim in range(len(vector)):
            vector[dim] = (vector[dim] - global_mean[dim]) / sqrt(global_variance[dim])
