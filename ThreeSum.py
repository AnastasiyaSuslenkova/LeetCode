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
    triplets = set()
    dict_nums = defaultdict(int, Counter(nums))
    nums_set = dict_nums.copy().keys()
    for p in nums_set:
        if p == 0:
            if dict_nums[0] > 2:
                triplets.add(frozenset([0]))
        else:
            for n in nums_set:
                if n != p:
                    k = -(n + p)
                    if (k == p) or (k == n): 
                        if dict_nums[k] > 1:
                            triplets.add(frozenset([p, n, k]))
                    elif dict_nums[k] > 0:
                        triplets.add(frozenset([p, n, k]))
    triplets_output = []
    for triplet in triplets:
        tr_out = list(triplet)
        while len(tr_out) < 3:
            tr_out.append(-sum(tr_out))
        triplets_output.append(tr_out)
    return triplets_output


if __name__ == '__main__':
    tests = [{'nums': [-1, 0, 1, 2, -1, -4], 'expected': [[-1, -1, 2], [-1, 0, 1]]},
             {'nums': [0, 1, 1], 'expected': []},
             {'nums': [0, 0, 0], 'expected': [[0, 0, 0]]},
             {'nums': [3, 0, -2, -1, 1, 2], 'expected': [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]}]
    for test in tests:
        print(test, three_sum(test['nums']))

