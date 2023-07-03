# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians).
# The soldiers are positioned in front of the civilians.
# That is, all the 1's will appear to the left of all the 0's in each row.

# A row i is weaker than a row j if one of the following is true:

# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.

# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

# Examples:

# Input: mat =
# [[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]],
# k = 3
# Output: [2,0,3]

# Input: mat =
# [[1,0,0,0],
#  [1,1,1,1],
#  [1,0,0,0],
#  [1,0,0,0]],
# k = 2
# Output: [0,2]


import numpy as np


def k_weakest_rows(mat: list[list[int]], k: int) -> list[int]:
    num_sold = np.array(mat).sum(axis=1)
    m = len(mat)
    return sorted(range(m), key=lambda i: num_sold[i])[:k]


if __name__ == '__main__':
    tests = [{'mat': [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 'k': 3, 'expected_result': [2,0,3]},
             {'mat': [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]], 'k': 2, 'expected_result': [0,2]}]
    for test in tests:
        print(test, k_weakest_rows(test['mat'], test['k']))
