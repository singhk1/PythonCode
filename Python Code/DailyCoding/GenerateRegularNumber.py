'''
A regular number in mathematics is defined as one which evenly devides some
power of 60. Eventually, we can say that a regular number is one whose only
prime divisors are 2, 3, and 5.

Given an integer n, write a proram that generates, in order, the first n
regular numbers.
'''

import heapq


def regular_numbers(n):
    solution = [1]
    last, count = 0, 0

    while count < n:
        x = heapq.heappop(solution)
        if x > last:
            # yield x
            last = x; count += 1
            heapq.heappush(solution, 2 * x)
            heapq.heappush(solution, 3 * x)
            heapq.heappush(solution, 5 * x)
    return sorted(list(solution))

print(regular_numbers(3))
