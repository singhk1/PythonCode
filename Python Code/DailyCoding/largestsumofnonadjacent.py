def largest(ls):
    if not ls:
        return 0
    return max(largest(ls[1:]), ls[0] + largest(ls[2:]))


def largest_elegant(ls):
    if len(ls) <= 2:
        return max(0, max(ls))

    cache = [0 for i in ls]
    cache[0] = max(0, ls[0])
    cache[1] = max(cache[0], ls[1])

    for i in range(2, len(ls)):
        num = ls[i]
        cache[i] = max(num + cache[i - 2], cache[i - 1])
    return cache[-1]

def largest_elegant2(ls):
    if len(ls) <= 2:
        return max(0, max(ls))
    max_excluding_last = max(0, ls[0])
    max_including_last = max(max_excluding_last, ls[1])

    for num in ls[2:]:
        prev_max_including_last = max_including_last
        max_including_last = max(max_including_last, max_excluding_last + num)
        max_excluding_last = prev_max_including_last
    return max(max_including_last, max_excluding_last)

ls = [2, 4, 6, 2, 5]
#print(largest(ls))
print(largest_elegant(ls))
print(largest_elegant2 (ls))
