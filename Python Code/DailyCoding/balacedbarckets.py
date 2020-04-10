def is_balance(str):
    stack = []
    for ch in str:
        if ch in ["(", "{", "["]:
            stack.append(ch)
        else:
            if not stack:
                return False
            if (ch == ")" and stack[-1] != "(") or \
                (ch == "}" and stack[-1] != "{") or \
                (ch == "]" and stack[-1] != "[") :
                return False
            stack.pop()
    return len(stack) == 0


str = "([])[]({})"
print(is_balance(str))
