'''
Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.

Example 1:

Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically.
 "HAY"
 "ORO"
 "WEU"
'''

def words_vertically(s):
    x = s.split()
    m = max(len(y) for y in x)
    print(m)
    res = [""] * m
    for i in range(m):
        for j in x:
            if i < len(j):
                res[i] += j[i]
            else:
                res[i] += " "
        res[i] = res[i].rstrip()
    return res

s = "HOW ARE YOU"
print(words_vertically(s))
