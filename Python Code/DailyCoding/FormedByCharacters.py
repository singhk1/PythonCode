'''
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation:
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
'''
from collections import Counter
def formed_by_charcters(words, chars):
    out = 0
    for word in words:
        test = []
        test_word = []
        for i in chars:
            test.append(i)

        for j in word:
            test_word.append(j)

        compare_word = []

        for k in test_word:
            if k in test:
                compare_word += k
                test.remove(k)
        if "".join(compare_word) == word:
            out += len(word)
    return out


def formed_by_charcters_better(words, chars):
    result = 0
    d = Counter(chars)

    for w in words:
        flag = True
        for i in w:
            if i not in d and w.count(i) > d[i]:
                flag = False
                break
        if flag:
            result += len(w)
    return result



words = ["cat","bt","hat","tree"]
chars = "attach"
print(formed_by_charcters(words, chars))

words = ["cat","bt","hat","tree"]
chars = "attach"
print(formed_by_charcters_better(words, chars))
