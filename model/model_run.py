from heapq import heappush, heappop
from random import sample


class HeapNode:
    def __init__(self, index, value):
        self.index = index
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value > other.value


def select_top_suggestions(historical_orders, menu_items, affinity_measure, num_elem):
    if len(historical_orders) == 0:
        # Random sample.
        print("Generating random sample for suggestions due to no historical data.")
        return list(sample(range(0, len(menu_items)), num_elem))

    pq = []
    for index in range(len(menu_items)):
        heappush(pq, HeapNode(index, affinity_measure(menu_items[index], historical_orders)))
    return [heappop(pq).index for _ in range(num_elem)]
