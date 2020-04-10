

def value(letter):
    return ord(letter) - 96

def simple_hash(prev, start, new):
    return prev - value(start) + value(new)

def find_matches(pattern, string):
    matches = []
    k = len(pattern)

    pattern_val = 0
    for i, char in enumerate(pattern):
        pattern_val += value(char)
    print(pattern_val)

    hash_value = 0
    for i, char in enumerate(string[:k]):
        hash_value += value(char)
    print(hash_value)

    if pattern_val == hash_value:
        if string[:k] == pattern:
            matches.append(0)
    print(matches)

    for i in range(len(string) - k):
        hash_value = simple_hash(hash_value, string[i], string[i + k])
        if hash_value == pattern_val:
            if string[i + 1 : i + k + 1] == pattern:
                matches.append(i + 1)
    return matches


st = "abracadabra"
pattern = "abr"
print(find_matches(pattern, st))
