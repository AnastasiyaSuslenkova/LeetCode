# You are given an m x n integer array grid.
# There is a robot initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.
#
# An obstacle and space are marked as 1 or 0 respectively in grid.
# A path that the robot takes cannot include any square that is an obstacle.
#
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
#
# The testcases are generated so that the answer will be less than or equal to 2 * 10^9.
#
#
# Example 1:
#
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#
# Example 2:
#
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
#
#
# Constraints:
#
#     m == obstacleGrid.length
#     n == obstacleGrid[i].length
#     1 <= m, n <= 100
#     obstacleGrid[i][j] is 0 or 1.

from itertools import dropwhile, product

import numpy as np


def unique_paths_with_obstacles(obstacle_grid: list[list[int]]) -> int:
    if (obstacle_grid[0][0] == 1) or (obstacle_grid[-1][-1] == 1):
        return 0
    n, m = len(obstacle_grid), len(obstacle_grid[0])
    ways_map = np.ones((n, m), dtype=int)
    for i in dropwhile(lambda x: obstacle_grid[x][0] == 0, range(n)):
        ways_map[i][0] = 0
    for j in dropwhile(lambda x: obstacle_grid[0][x] == 0, range(m)):
        ways_map[0][j] = 0
    for i, j in product(range(1, n), range(1, m)):
        if obstacle_grid[i][j] == 1:
            ways_map[i][j] = 0
        else:
            ways_map[i][j] = ways_map[i - 1][j] + ways_map[i][j - 1]
    return ways_map[-1][-1]


if __name__ == '__main__':
    tests = [{'obstacle_grid': [[0, 0, 0], [0, 1, 0], [0, 0, 0]], 'expected': 2},
             {'obstacle_grid': [[0, 1], [0, 0]], 'expected': 1},
             {'obstacle_grid': [[0, 1, 0], [0, 1, 0], [0, 0, 0]], 'expected': 1},
             {'obstacle_grid': [[1, 0, 0], [0, 0, 0], [0, 0, 0]], 'expected': 0},
             {'obstacle_grid': [[0, 0, 0], [0, 0, 0], [0, 0, 1]], 'expected': 0}]
    for test in tests:
        print(test, unique_paths_with_obstacles(test['obstacle_grid']))

