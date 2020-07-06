def value(letter, power):
    return (26 ** power) * (ord(letter) - 96)

def rabin_hash(prev, start, new, k):
    return (prev - value(start, k - 1)) * 26 + value(new, 0)

def find_matches(pattern, string):
    matches = []
    k = len(pattern)

    pattern_val = 0
    for i, char in enumerate(pattern):
        pattern_val += value(char, k - i - 1)
    #print(pattern_val)

    hash_value = 0
    for i, char in enumerate(string[:k]):
        hash_value += value(char, k - i - 1)

    #print(hash_value)

    if pattern_val == hash_value:
        if string[:k] == pattern:
            matches.append(0)

    for i in range(len(string) - k):
        hash_value = rabin_hash(hash_value, string[i], string[i + k], k)
        if pattern_val == hash_value:
            #print(str(pattern_val) + " " + str(hash_value))
            if string[i + 1 : i + k + 1] == pattern:
                matches.append(i + 1)
    return matches


st = "cabracadabra"
pattern = "abr"
print(find_matches(pattern, st))
