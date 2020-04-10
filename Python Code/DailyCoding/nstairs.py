def staircase(n):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    X = [1, 2]
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X)
    return cache[n]

print(staircase(3))
print(staircase(4))
