# Given an array of strings nums containing n unique binary strings
# each of length n, return a binary string of length n
# that does not appear in nums. If there are multiple answers,
# you may return any of them.
#
#
#
# Example 1:
#
# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.
#
# Example 2:
#
# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.
#
# Example 3:
#
# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100",
# and "110" would also be correct.
#
#
#
# Constraints:
#
#     n == nums.length
#     1 <= n <= 16
#     nums[i].length == n
#     nums[i] is either '0' or '1'.
#     All the strings of nums are unique.


def find_different_binary_string(nums: list[str]) -> str:
    len_nums = len(nums)
    for i in range(2 ** len_nums):
        i_binary = f'{i:0{len_nums}b}'
        if i_binary not in nums:
            return i_binary


if __name__ == '__main__':
    tests = [
        {'nums': ["01", "10"], 'expected': "11 or 00"},
        {'nums': ["00", "01"], 'expected': "11 or 10"},
        {'nums': ["111", "011", "001"], 'expected': "101, 000, 010, 100, or 110"}
    ]
    for test in tests:
        print(test, find_different_binary_string(test['nums']))
