# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside
# the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers
# (signed or unsigned).
#
# Example 1:
# Input: x = 123
# Output: 321
#
# Example 2:
# Input: x = -123
# Output: -321
#
# Example 3:
# Input: x = 120
# Output: 21
#
# Example 3:
# Input: x = 1534236469
# Output: 0
# Because 9646324351 > 2^31 - 1

import math


def reverse(x: int) -> int:
    sign = 1
    if x < 0:
        sign = -1
    y = abs(x)
    if y < 10:
        return x
    if (x < -(2 ** 31)) or x > ((2 ** 31) - 1):
        return 0
    len_x = int(math.log10(y))
    max_d = 10 ** len_x
    min_d = 1
    x = 0
    for _ in range(len_x + 1):
        x = x + ((y // max_d) % 10) * min_d
        max_d = max_d / 10
        min_d = min_d * 10
    x = int(x) * sign
    big_value = 2 ** 31
    if (x < -big_value) or (x > (big_value - 1)):
        return 0
    return x


if __name__ == '__main__':
    tests = {123: 321, -123: -321, 120: 21, 1534236469: 0}
    for inp, answer in tests.items():
        print(f'x: {inp}, expected: {answer}, output: {reverse(inp)}')
