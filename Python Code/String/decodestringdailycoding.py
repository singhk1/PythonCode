from collections import defaultdict
def num_encoding(s):
    if s.startswith('0'):
        return 0
    elif len(s) <= 1:
        return 1

    total = 0
    if int(s[:2]) <= 26:
        total += num_encoding(s[2:])
    total += num_encoding(s[1:])

    return total

def num_encodings(s):
    cache = defaultdict(int)
    cache[len(s)] = 1

    for i in reversed(range(len(s))):
        if s[i].startswith('0'):
            cache[i] = 0
        elif i == len(s) - 1:
            cache[i] = 1
        else:
            if int(s[i:i + 2]) <= 26:
                cache[i] = cache[i + 2]
            cache[i] += cache[i + 1]
    print(cache, end = ' ')
    return cache[0]

s = '11'
s1 = '626'
print(num_encoding(s))
print(num_encoding(s1))
print(num_encodings(s))
print(num_encodings(s1))
