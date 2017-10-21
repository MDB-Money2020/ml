from fb.firebase_model_classes import Order


def get_historic_orders(user_id):
    """
    Retrieve list of Orders of a User.
    :param user_id: The User's uid.
    :return:        list of Order objects.
    """
    # TODO
    order1 = Order('order_id!', 'lulz')
    order2 = Order('order_id2!', 'lulz2')
    order3 = Order('order_id3!', 'lulz3')
    order4 = Order('order_id4!', 'lulz4')
    return [order1, order2, order3, order4]


def get_menu_items_from_restaurant(restaurant_id):
    """
    Retrieve list of Orders of a Restaurant.
    :param restaurant_id: ID of the restaurant.
    :return:              List of Order objects.
    """
    order1 = Order('order_idsss!', 'lulz')
    order2 = Order('order_idsssss2!', 'lulz2')
    order3 = Order('order_idss3!', 'lulz3')
    return [order1, order2, order3]
