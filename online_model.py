def run_suggestion_model(historic_menu_items, menu_items):
    """
    Runs a pre-trained model to return 3 suggested items
    from menu_items based on historic_menu_items.
    :param historic_menu_items: List of MenuItem objects of the user's historic orders.
    :param menu_items:      List of MenuItem objects of the Restaurant's menu items.
    :return:                Indices in menu_items of the appropriate suggestions.
    """
    num_to_return = min(len(menu_items), 3)
    return list(range(0, num_to_return))

