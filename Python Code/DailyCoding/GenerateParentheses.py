'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

def generate_parentheses(n):
    res = []
    backtrack(res, "", 0, 0, n)
    return res



def backtrack(res, st, left, right, maximum):
    if len(st) == 2 * maximum:
        res.append(st)
        return

    if left < maximum:
        backtrack(res, st + '(', left + 1, right, maximum)
    if right < left:
        backtrack(res, st + ')', left, right + 1, maximum)

print(generate_parentheses(3))
