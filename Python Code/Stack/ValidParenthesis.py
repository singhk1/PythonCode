def paran(s):
    if s == "":
        return True

    stack = []
    stack_one = []
    for i, ch in enumerate(s):
        if ch == "(":
            stack.append(i)
        elif ch == "*":
            stack_one.append(i)
        else:
            if not stack and not stack_one:
                return False
            if stack:
                stack.pop()
            else:
                stack_one.pop()

    while stack and stack_one:
        if stack.pop() > stack_one.pop():
            return False
    return len(stack) == 0

def parentheses(s):
    if s == "":
        return True

    balance = 0

    for i in range(len(s)):
        if s[i] == "(":
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False

    if balance == 0:
        return True

    balance = 0

    for i in reversed(range(len(s))):
        if s[i] == "(":
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    return True


s = "()"
s1 = "(())((())()()(*)(*()(())())()()((()())((()))(*"
print(paran(s))
print(paran(s1))
print(parentheses(s))
print(parentheses(s1))
