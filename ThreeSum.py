# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
# and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
#
# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#
# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
#
# Constraints:
#
#     3 <= nums.length <= 3000
#     -10^5 <= nums[i] <= 10^5

from collections import Counter, defaultdict


def three_sum(nums: list[int]) -> list[list[int]]:
    triplets = []
    dict_nums = defaultdict(int, Counter(nums))
    pos_set = set()
    neg_set = set()
    for n in dict_nums.keys():
        if n > 0:
            pos_set.add(n)
        elif n < 0:
            neg_set.add(n)
    if dict_nums[0] > 2:
        triplets.append([0, 0, 0])
    for p in pos_set:
        for n in neg_set:
            if (-(n + p) == p or -(n + p) == n) and (dict_nums[-(n + p)] > 1):
                triplets.append([p, n, -(n + p)])
            elif dict_nums[-(n + p)] > 0:
                if (-(n + p) < p) and (-(n + p) > n):
                    triplets.append([p, n, -(n + p)])
    return triplets


if __name__ == '__main__':
    tests = [{'nums': [-1, 0, 1, 2, -1, -4], 'expected': [[-1, -1, 2], [-1, 0, 1]]},
             {'nums': [0, 1, 1], 'expected': []},
             {'nums': [0, 0, 0], 'expected': [[0, 0, 0]]},
             {'nums': [3, 0, -2, -1, 1, 2], 'expected': [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]}]
    for test in tests:
        print(test, three_sum(test['nums']))

