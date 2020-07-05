'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''

def longest(st):
    stack = [-1]
    l = 0
    for i in range(len(st)):
        if st[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                l = max(l, i - stack[-1])
    return l

st = "(()"
print(longest(st))
print(longest(")()())"))
