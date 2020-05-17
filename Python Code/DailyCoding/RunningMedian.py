'''
calculate running median of a stream
[2, 1, 5, 7, 2, 0, 5]

'''
import heapq

def running_median(array):
    min_meap = []
    max_heap = []
    for i in array:
        add(i, min_meap, max_heap)
        rebalance(min_meap, max_heap)
        print_median(min_meap, max_heap)

def add(num, min_meap, max_heap):
    if len(min_meap) + len(max_heap) < 1:
        heapq.heappush(min_meap, num)
        return
    median = get_median(min_meap, max_heap)

    if num > median:
        heapq.heappush(min_meap, num)
    else:
        heapq.heappush(max_heap, -1 * num)


def get_median(min_meap, max_heap):
    if len(min_meap) > len(max_heap):
        return min_meap[0]
    elif len(max_heap) > len(min_meap):
        return -1 * max_heap[0]
    else:
        return (min_meap[0] + -1 * max_heap[0]) / 2.0

def rebalance(min_meap, max_heap):
    if len(min_meap) > len(max_heap) + 1:
        root = heapq.heappop(min_meap)
        heapq.heappush(max_heap, -1 * root)
    elif len(max_heap) > len(min_meap) + 1:
        root = -1 * heapq.heappop(max_heap)
        heapq.heappush(min_meap, root)

def print_median(min_meap, max_heap):
    print(get_median(min_meap, max_heap))


array = [2, 1, 5, 7, 2, 0, 5]
running_median(array)
