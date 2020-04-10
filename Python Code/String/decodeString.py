from collections import deque
def decode(s):
    if not s:
        return 'hello'
    res = ''
    count = 0
    for i in s:
        if i.isdigit():
            count = count * 10 + int(i)
        else:
            res += i * count
            count = 0
    return res

def encode(s):
    if not s:
        return "hello"
    result = ''
    curr_char = s[0]
    curr_count = 0
    for i, char in enumerate(s, 1):
        if char == curr_char:
            curr_count += 1
        else:
            result += str(curr_count) + curr_char
            curr_char = char
            curr_count = 1
    result += str(curr_count) + curr_char
    return result

def decodestringleetcode(s):
    if not s:
        return ''
    stack = deque([])
    for i in s:
        if i != ']':
            stack.append(i)
        else:
            seq = ""
            while stack[-1] != '[':
                seq = stack.pop() + seq
            stack.pop()
            times = ""
            while stack and stack[-1].isdigit():
                times = stack.pop() + times
            stack.append(int(times) * seq)
    return ''.join(stack)

s = "4ab3bd2j1u"
s1 = ""
s2 = "AAAABBBCCDAA"
s3 ="2[abc]3[cd]ef"
print(decode(s))
print(decode(s1))
print(encode(s2))
print(decodestringleetcode(s3))
