def longest(s):
    if not s:
        return 0
    stack = [-1]
    length = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                length = max(length, i - stack[-1])
    return length


s = ')()())'
print(longest(s))
