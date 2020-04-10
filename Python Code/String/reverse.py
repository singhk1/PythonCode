def rev(s, k):
    a = list(s)
    length = len(a)
    for i in range(0, length, 2*k):
        a[i:i+k] = reversed(a[i:i+k])
    return "".join(a)

s = "abcdefgh"
print(rev(s, 3))
