'''
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
'''
def min_distance(word1, word2):
    my_arr = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]

    for i in range(len(word1) + 1):
        for j in range(len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                my_arr[i][j] = my_arr[i -1][j - 1]
            else:
                my_arr[i][j] = 1 + min(my_arr[i - 1][j], my_arr[i][j - 1], my_arr[i - 1][j - 1])
    return my_arr[len(word1)][len(word2)]


word1 = "horse"
word2 = "ros"
print(min_distance(word1, word2))
