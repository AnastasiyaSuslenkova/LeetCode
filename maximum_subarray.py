# Given an integer array nums, find the subarray with the largest sum, and return its sum.
#
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
#
# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
#
# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
#
# Constraints:
#     1 <= nums.length <= 10^5
#     -10^4 <= nums[i] <= 10^4


def max_sub_array(nums: list[int]) -> int:
    sums_subarray = set()
    sum_subarray = 0
    for n in nums:
        sum_subarray = sum_subarray + n
        sums_subarray.add(sum_subarray)
        sum_subarray = max(sum_subarray, 0)
    return max(sums_subarray)


if __name__ == '__main__':
    tests = [{'nums': [-2, 1, -3, 4, -1, 2, 1, -5, 4], 'expected': 6},
             {'nums': [1], 'expected': 1},
             {'nums': [5, 4, -1, 7, 8], 'expected': 23}]
    for test in tests:
        print(test, max_sub_array(test['nums']))

