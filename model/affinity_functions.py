import numpy as np


def cosine_similarity(x, y):
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    return x.dot(y) / (norm_x * norm_y)


def avg_cos_sim_affinity(menu_item_vec, historical_orders_vecs):
    total_cosine_sim = 0
    for historical_order_vec in historical_orders_vecs:
        total_cosine_sim += cosine_similarity(menu_item_vec, historical_order_vec)
    return total_cosine_sim / len(historical_orders_vecs)