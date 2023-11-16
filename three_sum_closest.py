# Given an integer array nums of length n and an integer target,
# find three integers in nums such that the sum is closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.
#
#
#
# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
#
#
# Constraints:
#
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4


import math


def three_sum_closest(nums: list[int], target: int) -> int:
    len_nums = len(nums)
    assert len_nums >= 3
    nums_sorted = sorted(nums)
    min_difference = math.inf
    for i, n_i in enumerate(nums_sorted[:len_nums - 2]):
        j, k = i + 1, len_nums - 1
        while j < k:
            val = n_i + nums_sorted[j] + nums_sorted[k]
            if val == target:
                return val
            if val > target:
                k -= 1
            else:
                j += 1
            difference = abs(target - val)
            if difference < min_difference:
                min_difference = difference
                value = val
    return value


if __name__ == '__main__':
    tests = [
        {'nums': [-1, 2, 1, -4], 'target': 1, 'expected': 2},
        {'nums': [0, 0, 0], 'target': 1, 'expected': 0},
    ]
    for test in tests:
        print(test, three_sum_closest(test['nums'], test['target']))
