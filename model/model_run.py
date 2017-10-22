from heapq import heapify, heappush, heappop


class HeapNode:
    def __init__(self, index, value):
        self.index = index
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


def select_top_suggestions(historical_orders, menu_items, affinity_measure, num_elem):
    pq = heapify([])
    for index in range(len(menu_items)):
        heappush(pq, HeapNode(index, affinity_measure(menu_items[index], historical_orders)))
    return [heappop(pq).value for _ in range(num_elem)]
