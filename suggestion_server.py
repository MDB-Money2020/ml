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
    :return: jsonified array of menuIds.
    """
    user_id = request.values.get('userId', None)
    restaurant_id = request.values.get('restaurantId', None)
    if not user_id or not restaurant_id:
        return '', status.HTTP_400_BAD_REQUEST
    else:
        try:
            suggested_menu_ids = get_suggestion_items(user_id, restaurant_id)
            return json.dumps(suggested_menu_ids), status.HTTP_200_OK
        except Exception as e:
            suggestion_server_app.log_exception(e)
            return '', status.HTTP_500_INTERNAL_SERVER_ERROR


def get_suggestion_items(user_id, restaurant_id):
    """
    Returns an array of menu_item_ids.
    :param user_id:       Id of the user.
    :param restaurant_id: Id of the restaurant.
    :return:              Array of menu item ids.
    """
    historic_orders = get_historic_menu_items(user_id)
    menu_items = get_menu_items_from_restaurant(restaurant_id)
    menu_items_indices = run_suggestion_model(historic_orders, menu_items)
    menu_item_ids = [menu_items[i].menu_item_id for i in menu_items_indices]
    return menu_item_ids


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    suggestion_server_app.run(port=port)
