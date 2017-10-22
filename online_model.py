from model.feature_gen import construct_feature_vectors, normalize_demean
from model.model_run import select_top_suggestions
from model.affinity_functions import avg_cos_sim_affinity


def run_suggestion_model(historic_menu_items, menu_items):
    """
    Runs a pre-trained model to return 3 suggested items
    from menu_items based on historic_menu_items.
    :param historic_menu_items: List of MenuItem objects of the user's historic orders.
    :param menu_items:      List of MenuItem objects of the Restaurant's menu items.
    :return:                Indices in menu_items of the appropriate suggestions.
    """
    num_to_return = min(len(menu_items), 3)
    historical_orders_vecs = construct_feature_vectors(historic_menu_items)
    menu_item_vecs = construct_feature_vectors(menu_items)
    normalize_demean(historical_orders_vecs)
    normalize_demean(menu_item_vecs)
    return select_top_suggestions(historical_orders_vecs, menu_item_vecs, avg_cos_sim_affinity, num_to_return)
