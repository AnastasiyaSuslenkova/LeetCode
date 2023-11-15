# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted,
# you need to do the following things:
#     Change the array nums such that the first k elements of nums contain
#     the unique elements in the order they were present in nums initially.
#     The remaining elements of nums are not important as well as the size of nums.
#     Return k.
#
# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2,
# with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
#
# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5,
# with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
#
# Constraints:
#     1 <= nums.length <= 3 * 104
#     -100 <= nums[i] <= 100
#     nums is sorted in non-decreasing order.


# Первый вариант - использую np.unique(), выглядит коротко, но работает долго,
# видимо, из-за импорта
import numpy as np


def remove_duplicates1(nums: list[int]) -> int:
    nums[0:] = np.unique(nums)
    return len(nums)


# Второй вариант, менее красивый, но время работы раза в два меньше
# (если строчку с импортом тоже убрать)
def remove_duplicates2(nums: list[int]) -> int:
    nums_orig = nums.copy()
    i = 0
    for n in nums_orig:
        if n != nums[i]:
            nums[i + 1] = n
            i += 1
    return i + 1


if __name__ == '__main__':
    inp = 'nums'
    tests = [
        {inp: [1, 1, 2], 'expected_k': 2, 'expected_nums': [1, 2]},
        {inp: [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 'expected_k': 5,
         'expected_nums': [0, 1, 2, 3, 4]}
    ]
    for test in tests:
        print(test)
        print(f'k = {remove_duplicates1(test[inp])}')
        print(f'nums = {test[inp]}')
