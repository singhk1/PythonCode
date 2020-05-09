'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''

def reverseS(s):
    s = s.split()
    for i in range(len(s)):
        s[i] = s[i][::-1]
        print(s[i])
    return " ".join(s)

s = "Let's take LeetCode contest"
print(reverseS(s))
