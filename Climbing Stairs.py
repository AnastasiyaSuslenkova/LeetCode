# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
# Constraints:
#     1 <= n <= 45


def climb_stairs(n: int) -> int:
    if n < 3:
        return n
    prev_ways = 1
    ways = 2
    for i in range(2, n):
        ways, prev_ways = ways + prev_ways, ways
    return ways


if __name__ == '__main__':
    tests = {2: 2, 3: 3, 4: 5, 5: 8, 10: 89}
    for inp, exp in tests.items():
        print(f'n: {inp}, expected: {exp}, output: {climb_stairs(inp)}')

