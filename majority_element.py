# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
#
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


from statistics import mode


def majority_element(nums: list[int]) -> int:
    return mode(nums)


if __name__ == '__main__':
    tests = [{'inp': [3, 2, 3], 'expected': 3},
             {'inp': [2, 2, 1, 1, 1, 2, 2], 'expected': 2}]
    for test in tests:
        print(test, majority_element(test['inp']))
