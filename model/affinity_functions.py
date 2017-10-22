import numpy as np


def cosine_similarity(x, y):
    """
    Returns the cosine similarity score between vector x and y.
    Assumes nonzero x and y.
    :param x: numpy array of first vector.
    :param y: numpy array of second vector.
    :return:  scalar representing the cosine similarity score.
    """
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    if norm_x > 0 and norm_y > 0:
        return x.dot(y) / (norm_x * norm_y)


def avg_cos_sim_affinity(menu_item_vec, historical_orders_vecs):
    """
    An affinity measure that takes the average cosine similarity between
    a menu item and the historical order vectors.
    Assumes the historical_orders_vecs list is nonempty.
    :param menu_item_vec:          np array of the menu item feature vector.
    :param historical_orders_vecs: np array of the historical item feature vector.
    :return:                       scalar of the average cosine similarity.
    """
    total_cosine_sim = 0
    for historical_order_vec in historical_orders_vecs:
        total_cosine_sim += cosine_similarity(menu_item_vec, historical_order_vec)
    return total_cosine_sim / len(historical_orders_vecs)
