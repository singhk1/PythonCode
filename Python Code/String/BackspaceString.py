def build(st):
    s = []
    for c in st:
        if c != '#':
            s.append(c)
        elif s != []:
            s.pop()
    return str(s)


st = "ab##c"
print(build(st))
