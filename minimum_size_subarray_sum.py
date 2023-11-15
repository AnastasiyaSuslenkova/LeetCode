# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
#
# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1
#
# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
#
# Example 4:
# Input: target = 213, nums = [12,28,83,4,25,26,25,2,25,25,25,12]
# Output: 8
#
#
# Constraints:
#    1 <= target <= 10^9
#    1 <= nums.length <= 10^5
#   1 <= nums[i] <= 10^4

# Важно, что тут имеется в виду, что элементы подмассива должны идти подряд в массиве (иначе бы решение было проще)


def min_subarray_len(target: int, nums: list[int]) -> int:
    sum_arr = 0
    i = 0
    len_arrs = []
    arr = []
    while i < len(nums):
        while (sum_arr < target) and (i < len(nums)):
            arr.append(i)
            sum_arr += nums[i]
            i += 1
        j = -1
        while sum_arr >= target:
            j += 1
            sum_arr = sum_arr - nums[arr[j]]
        if j > -1:
            len_arrs.append(len(arr[j:]))
        arr = arr[j + 1:]
        if len(len_arrs) == 0:
            return 0
    return min(len_arrs)


if __name__ == '__main__':
    tests = [{'target': 7, 'nums': [2, 3, 1, 2, 4, 3], 'expected': 2},
             {'target': 4, 'nums': [1, 4, 4], 'expected': 1},
             {'target': 11, 'nums': [1, 1, 1, 1, 1, 1, 1, 1], 'expected': 0},
             {'target': 213, 'nums': [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12], 'expected': 8}]
    for test in tests:
        print(test, min_subarray_len(test['target'], test['nums']))
