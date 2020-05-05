def fib_bottomup(n):
    f = [0] * (n + 1)
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

cache = {}
def fib_memoization(n):

    if n in cache:
        return cache[n]
    if n == 1:
        val = 1
    elif n == 2:
        val = 1
    elif n > 2:
        val = fib_memoization(n - 1) + fib_memoization(n - 2)
    cache[n] = val
    return val



# print(fib_bottomup(50))
for i in range(1, 101):
    # print(i, ":", fib_memoization(i))
    print(i, ":", fib_memoization(i))
