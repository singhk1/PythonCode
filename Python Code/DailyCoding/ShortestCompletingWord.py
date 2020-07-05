'''
Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate. Such a word is said to complete the given string licensePlate

Here, for letters we ignore case. For example, "P" on the licensePlate still matches "p" on the word.

It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in the array.

The license plate might have the same letter occurring multiple times. For example, given a licensePlate of "PP", the word "pair" does not complete the licensePlate, but the word "supper" does.

Example 1:
Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
Output: "steps"
Explanation: The smallest length word that contains the letters "S", "P", "S", and "T".
Note that the answer is not "step", because the letter "s" must occur in the word twice.
Also note that we ignored case for the purposes of comparing whether a letter exists in the word.
'''

def shortestCompletingWord(licensePlate, words):
    licensePlate = licensePlate.lower()
    words.sort(key = len)
    for i in words:
        flag = True
        for j in licensePlate:
            if j.isalpha():
                if j not in i or licensePlate.count(j) > i.count(j):
                    flag = False
        if flag:
            return i

licensePlate = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]
print(shortestCompletingWord(licensePlate, words))
licensePlate = "1s3 456"
words = ["looks", "pest", "stew", "show"]
print(shortestCompletingWord(licensePlate, words))
