# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
#
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#
# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
# Constraints:
#     0 <= nums.length <= 10^5
#     -10^9 <= nums[i] <= 10^9
from collections import defaultdict


def longest_consecutive(nums: list[int]) -> int:
    if not nums:
        return 0
    dict_key_max_value_min = defaultdict(bool)
    dict_key_min_value_max = defaultdict(bool)
    ns = set(nums)
    for n in ns:
        if type(dict_key_min_value_max[n + 1]) == int:
            if dict_key_max_value_min[n - 1]:
                dict_key_max_value_min[dict_key_min_value_max[n + 1]] = dict_key_max_value_min[n - 1]
                dict_key_min_value_max[dict_key_max_value_min[n - 1]] = dict_key_min_value_max[n + 1]
                dict_key_min_value_max[n + 1] = False
                dict_key_max_value_min[n - 1] = False
            else:
                this_max = dict_key_min_value_max[n + 1]
                dict_key_min_value_max[n] = this_max
                dict_key_max_value_min[this_max] = n
                dict_key_min_value_max[n + 1] = False
        elif type(dict_key_max_value_min[n - 1]) == int:
            this_min = dict_key_max_value_min[n - 1]
            dict_key_max_value_min[n] = this_min
            dict_key_min_value_max[this_min] = n
            dict_key_max_value_min[n - 1] = False
        else:
            dict_key_min_value_max[n] = n
            dict_key_max_value_min[n] = n
    res = 0
    for k, v in dict_key_min_value_max.items():
        if (type(v) == int) and ((v - k) > res):
            res = v - k
    return res + 1


if __name__ == '__main__':
    tests = [{'inp': [100, 4, 200, 1, 3, 2], 'exp': 4},
             {'inp': [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 'exp': 9}]
    for test in tests:
        print(test, longest_consecutive(test['inp']))

# выглядит страшно, но вроде как должно за O(n) работать (требование есть такое),
# если посмотреть значение по ключу у defaultdict - O(1)