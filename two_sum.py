# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.
#
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

def two_sum(nums: list[int], target: int) -> list[int]:
    for i, ni in enumerate(nums):
        for j in range(i):
            if ni + nums[j] == target:
                return [j, i]
    return []


if __name__ == '__main__':
    tests = [{'nums': [2, 7, 11, 15], 'target': 9, 'expected': [0, 1]},
             {'nums': [3, 2, 4], 'target': 6, 'expected': [1, 2]},
             {'nums': [3, 3], 'target': 6, 'expected': [0, 1]}]
    for test in tests:
        print(test, two_sum(test['nums'], test['target']))
