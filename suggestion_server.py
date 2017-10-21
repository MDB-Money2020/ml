from flask import Flask, request
from flask_api import status
import os
from fb.firebase_functions import *
from online_model import run_suggestion_model
import json


suggestion_server_app = Flask(__name__)


@suggestion_server_app.route('/', methods=['GET', 'POST'])
def retrieve_command():
    """
    Endpoint function for GET requests. Requires parameters:
    1. userId,
    2. restaurantId
    :return: jsonified array of orderIds.
    """
    user_id = request.values.get('userId', None)
    restaurant_id = request.values.get('restaurantId', None)
    if not user_id or not restaurant_id:
        return '', status.HTTP_400_BAD_REQUEST
    else:
        suggested_order_ids = get_suggestion_items(user_id, restaurant_id)
        return json.dumps(suggested_order_ids), status.HTTP_200_OK


def get_suggestion_items(user_id, restaurant_id):
    """
    Returns an array of order_ids.
    :param user_id:       Id of the user.
    :param restaurant_id: Id of the restaurant.
    :return:              Array of order ids.
    """
    historic_orders = get_historic_orders(user_id)
    menu_items = get_menu_items_from_restaurant(restaurant_id)
    menu_items_indices = run_suggestion_model(historic_orders, menu_items)
    order_ids = [menu_items[i].order_id for i in menu_items_indices]
    return order_ids


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    suggestion_server_app.run(port=port)
