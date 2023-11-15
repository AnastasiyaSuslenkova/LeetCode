# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#
# Example 3:
# Input: nums = [1, 2], k = 3
# Output: [3, 1]
# Explanation:
# rotate 1 steps to the right: [2, 1]
# rotate 2 steps to the right: [1, 2]
# rotate 3 steps to the right: [2, 1]
#
# Constraints:
#     1 <= nums.length <= 105
#     -231 <= nums[i] <= 231 - 1
#     0 <= k <= 105

def rotate(nums: list[int], k: int) -> None:
    k = k % len(nums)
    nums[k + 1:], nums[:k + 1] = nums[:-k], nums[-k:]


if __name__ == '__main__':
    input1 = 'nums'
    tests = [{'nums': [1, 2, 3, 4, 5, 6, 7], 'k': 3, 'expected': [5, 6, 7, 1, 2, 3, 4]},
             {'nums': [-1, -100, 3, 99], 'k': 2, 'expected': [3, 99, -1, -100]},
             {'nums': [1, 2], 'k': 3, 'expected': [2, 1]}]
    for test in tests:
        print(test)
        rotate(test['nums'], test['k'])
        print(f'output: {test[input1]}')
