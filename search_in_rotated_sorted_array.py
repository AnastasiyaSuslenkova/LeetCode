# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
# or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
#
# Constraints:
#     1 <= nums.length <= 5000
#     -10^4 <= nums[i] <= 10^4
#     All values of nums are unique.
#     nums is an ascending array that is possibly rotated.
#     -10^4 <= target <= 10^4


def search(nums: list[int], target: int) -> int:
    len_nums = len(nums)
    left, right = 0, len_nums - 1
    while (right - left) > 1:
        middle = (right + left) // 2
        if nums[middle] > nums[left]:
            left = middle
        else:
            right = middle
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    right, left = left, right - len_nums
    while (right - left) > 1:
        middle = (right + left) // 2
        if nums[middle] == target:
            if middle < 0:
                return len_nums + middle
            return middle
        if nums[middle] > target:
            right = middle
        else:
            left = middle
    return -1


if __name__ == '__main__':
    tests = [{'nums': [4, 5, 6, 7, 0, 1, 2], 'target': 0, 'expected': 4},
             {'nums': [4, 5, 6, 7, 0, 1, 2], 'target': 3, 'expected': -1},
             {'nums': [1], 'target': 0, 'expected': -1}]
    for test in tests:
        print(test, search(test['nums'], test['target']))


# Without time complexity requirement there is a shorter solution:

# def search(nums: list[int], target: int) -> int:
#     try:
#         return nums.index(target)
#     except ValueError:
#         return -1'''
