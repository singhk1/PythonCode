import collections
def character_replacement(str, k):
    start = max_count = res = 0
    count = collections.Counter()
    for i, ch in enumerate(str):
        count[ch] += 1
        max_count = max(max_count, count[ch])
        while (i - start + 1) - max_count > k:
            count[start] -= 1
            start += 1
        res = max(res, i - start + 1)
    return res


str1 = "ABAB"
str2 = "ABABBA"
print(character_replacement(str1, 2))
print(character_replacement(str2, 1))
