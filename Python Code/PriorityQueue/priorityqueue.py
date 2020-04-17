import heapq

q = []
heapq.heappush(q, (2, 'code'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))
heapq.heappush(q, (0, 'sleep'))
while q:
    item = heapq.heappop(q)
    print(item)
