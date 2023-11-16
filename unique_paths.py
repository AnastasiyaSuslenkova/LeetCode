# There is a robot on an m x n grid. The robot is initially located
# at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths
# that the robot can take to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than
# or equal to 2 * 10^9.
#
# Example 1:
# Input: m = 3, n = 7
# Output: 28
#
# Example 2:
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways
# to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
#
# Example 2:
# Input: m = 23, n = 12
# Output: 193536720
#
# Constraints:
#     1 <= m, n <= 100
import math


def unique_paths(m: int, n: int) -> int:
    return math.comb(n + m - 2, n - 1)


if __name__ == '__main__':
    tests = [{'m': 3, 'n': 7, 'expected':  28},
             {'m': 3, 'n': 2, 'expected':  3},
             {'m': 23, 'n': 12, 'expected':  193536720}]
    for test in tests:
        print(test, unique_paths(test['m'], test['n']))
