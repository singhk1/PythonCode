
def find_matches(pattern, st):
    matches = []
    k = len(pattern)
    for i in range(len(st) - k + 1):
        if st[i : i + k] == pattern:
            matches.append(i)
    return matches

st = "abracadabra"
pattern = "abr"
print(find_matches(pattern, st))
