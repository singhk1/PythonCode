def parentheses(s):
    stack = []
    ls = list(s)
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        if char == ')':
            if len(stack) > 0:
                _ = stack.pop()
            else:
                ls[i] = '#'
    while stack:
        ls[stack.pop()] = '#'
    return ''.join([c for c in ls if c != '#'])

def parentheses2(s):
    ls = list(s)
    count = 0
    for i in range(len(ls)):
        if ls[i] == '(':
            count += 1
        elif ls[i] == ')':
            if count == 0:
                ls[i] = ""
            else:
                count -= 1
    l = len(ls) - 1
    while count > 0 and i >=0:
        if ls[i] == '(':
            ls[i] = ""
            count -= 1
        i -= 1
    if count > 0:
        return ""
    return ''.join(ls)


s = "lee(t(c)o)de)"
s1 = "lee((t(c)o)de)"
s2 = "lee(t(c)o)de)))))"
print(parentheses(s2))
print(parentheses2(s2))
