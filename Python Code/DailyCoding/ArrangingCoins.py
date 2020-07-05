'''
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
'''
'''
Using binary search:
Assume that the answer is kk, i.e. we've managed to complete kk rows of coins. These completed rows contain in total 1 + 2 + ... + k = \frac{k (k + 1)}{2}1+2+...+k=
2
k(k+1)
​
  coins.

We could now reformulate the problem as follows:

Find the maximum kk such that \frac{k (k + 1)}{2} \le N
2
k(k+1) <= N
'''

def arrangecoins_usingbinarysearch(n):
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        curr = mid * (mid + 1) // 2
        if curr == n:
            return mid
        if n < curr:
            right = mid - 1
        else:
            left = mid + 1
    return right

print(arrangecoins_usingbinarysearch(8))

'''
Using Math
K(K + 1) <= 2N
(k + 1/2)**2 - 1/4 <= 2N
k <= Sqrt(2N + 1/4) - 1/2


'''
import math
def arrangecoins_usingMath(n):
    return (int)(math.sqrt(2*n + 1/4) - 1/2)


print(arrangecoins_usingMath(8))
