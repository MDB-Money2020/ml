from heapq import heappush, heappop
from random import sample


class HeapNode:
    """
    A HeapNode object is used to provide a comparator based on score
    for a priority queue.
    """
    def __init__(self, index, value):
        self.index = index
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        """
        Less than in this context is defined as the value of self being greater
        than the other value.
        :param other: HeapNode we are comparing with.
        :return:      Conditional on whether self.value is greater than other.value.
        """
        return self.value > other.value


def select_top_suggestions(historical_orders, menu_items, affinity_measure, num_elem):
    """
    Select the top num_elem suggestions based on the passed in affinity_measure.
    :param historical_orders: List of numpy arrays of historical menu item vectors for a User.
    :param menu_items:        List of numpy arrays of menu item vectors for items in a Restaurant.
    :param affinity_measure:  Function that computes an affinity score for a menu item vs. historical_orders.
    :param num_elem:          Number of elements to suggest.
    :return:                  Indices in menu_items of top num_elem suggestions.
    """
    if len(historical_orders) == 0:
        # Random sample.
        print("Generating random sample for suggestions due to no historical data.")
        return list(sample(range(0, len(menu_items)), num_elem))

    pq = []
    for index in range(len(menu_items)):
        heappush(pq, HeapNode(index, affinity_measure(menu_items[index], historical_orders)))
    return [heappop(pq).index for _ in range(num_elem)]
