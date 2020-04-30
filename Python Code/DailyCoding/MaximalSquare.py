'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''

def maximal_square(matrix):
    rows = len(matrix)
    if rows == 0:
        return 0
    cols = len(matrix[0])
    maximum = 0
    dp = [[0] * (cols + 1) for i in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i - 1][j - 1] == 1:
                dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1
                if maximum < dp[i][j]:
                    maximum = dp[i][j]
    return maximum * maximum


matrix = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
print(maximal_square(matrix))
