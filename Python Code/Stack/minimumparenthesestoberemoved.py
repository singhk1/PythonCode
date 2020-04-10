def parentheses_count(s):
    ls = list(s)
    open , close = 0, 0
    for i in s:
        if i == '(':
            open += 1
        elif i == ')':
            if open:
                open -= 1
            else:
                close += 1

    return open + close

s = '((('
print(parentheses_count(s))
