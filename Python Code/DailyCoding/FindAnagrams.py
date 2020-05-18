'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
'''
from collections import Counter, defaultdict
def find_anagrams(s, word):
    w_len, s_len  = len(word), len(s)
    if s_len < w_len:
        return []

    w_count = Counter(word)
    s_count = Counter()

    res = []
    for i in range(s_len):
        s_count[s[i]] += 1
        if i >= w_len:
            if s_count[s[i - w_len]] == 1:
                del s_count[s[i - w_len]]
            else:
                s_count[s[i - w_len]] -= 1
        if s_count == w_count:
            res.append(i - w_len + 1)
    return res


def del_if_zero(dict, char):
    if dict[char] == 0:
        del dict[char]


def find_anagrams2(s, word):
    res = []
    freq = defaultdict(int)

    for char in word:
        freq[char] += 1

    for char in s[:len(word)]:
        freq[char] -= 1
        del_if_zero(freq, char)

    if not freq:
        res.append(0)

    for i in range(len(word), len(s)):
        start, end = s[i - len(word)], s[i]
        freq[start] += 1
        del_if_zero(freq, start)

        freq[end] -= 1
        del_if_zero(freq, end)

        if not freq:
            start_idx = i - len(word) + 1
            res.append(start_idx)
    return res



s = "cbaebabacd"
p = "abc"
print(find_anagrams(s, p))
print(find_anagrams2(s, p))
