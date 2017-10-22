from fb.firebase_model_classes import MenuItem
from urllib.parse import urlencode
from urllib.request import urlopen
import json

MENU_ITEMS_URL = "http://money2020-app.herokuapp.com/menuitems/"
USER_KEY = "userId"
RESTAURANT_KEY = "restaurantId"


def get_historic_menu_items(user_id):
    """
    Retrieve list of MenuItems of a User.
    :param user_id: The User's uid.
    :return:        list of MenuItem objects.
    """
    return get_menu_items_from_url(MENU_ITEMS_URL, {USER_KEY: user_id})


def get_menu_items_from_restaurant(restaurant_id):
    """
    Retrieve list of Menu Items of a Restaurant.
    :param restaurant_id: ID of the restaurant.
    :return:              List of MenuItem objects.
    """
    return get_menu_items_from_url(MENU_ITEMS_URL, {RESTAURANT_KEY: restaurant_id})


def get_menu_items_from_url(url, query_params):
    """
    Get a list of menu items from a url with query parameters.
    :param url:          URL that represents an API endpoint to get menu items.
    :param query_params: Query parameters to filter.
    :return:             List of Menu Item objects.
    """
    params = urlencode(query_params)
    url_manager = urlopen(url + '?' + params)
    json_array_response = url_manager.read()
    menu_item_dict_array = json.loads(json_array_response)
    menu_items = [MenuItem.construct_from_dict(menu_item_dict) for menu_item_dict in menu_item_dict_array]
    return menu_items

