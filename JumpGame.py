# You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
#
# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what.
# Its maximum jump length is 0, which makes it impossible to reach the last index.
#
# Constraints:
#     1 <= nums.length <= 10^4
#     0 <= nums[i] <= 10^5

import numpy as np


def can_jump(nums: list[int]) -> bool:
    nums_numpy = np.array(nums[:-1])
    for i in np.arange(len(nums_numpy))[nums_numpy == 0]:
        j = i - 1
        while (j >= 0) and (nums_numpy[j] < i - j + 1):
            j -= 1
        if j < 0:
            return False
    return True


if __name__ == '__main__':
    tests = [{'nums': [2, 3, 1, 1, 4], 'expected': True},
             {'nums': [3, 2, 1, 0, 4], 'expected': False},
             {'nums': [2, 0, 0], 'expected': True}]
    for test in tests:
        print(test, can_jump(test['nums']))

