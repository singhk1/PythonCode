from collections import Counter


def ransom_note(st, mag):
    my_map = Counter(mag)
    print(my_map)

    for i in st:
        if my_map[i] == 0:
            return False
        else:
            my_map[i] -= 1
    return True


st = "aa"
mag = "aba"
print(ransom_note(st, mag))
