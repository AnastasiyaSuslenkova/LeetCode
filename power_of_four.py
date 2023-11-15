# Given an integer n, return true if it is a power of four. Otherwise, return false.
#
# An integer n is a power of four, if there exists an integer x such that n == 4x.
#
#
#
# Example 1:
# Input: n = 16
# Output: true
#
# Example 2:
# Input: n = 5
# Output: false
#
# Example 3:
# Input: n = 1
# Output: true
#
# Example 4:
# Input: n = -64
# Output: false
#
#
# Constraints:
#
# -2^31 <= n <= 2^31 - 1
#
#
# Follow up: Could you solve it without loops/recursion?


import math


def is_power_of_four(n: int) -> bool:
    i = 1
    while i < n:
        i *= 4
    if i == n:
        return True
    return False


def is_power_of_four_without_loops(n: int) -> bool:
    if n <= 0:
        return False
    if math.log(n, 4).is_integer():
        return True
    return False


if __name__ == '__main__':
    tests = [
        {'n': 16, 'expected': True},
        {'n': 5, 'expected': False},
        {'n': 1, 'expected': True},
        {'n': -64, 'expected': False}
    ]
    for test in tests:
        print(test, is_power_of_four_without_loops(test['n']))
