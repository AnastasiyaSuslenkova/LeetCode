# Given an integer x, return true if x is a palindrome, and false otherwise.
#
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#
# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121.
# From right to left, it becomes 121-. Therefore it is not a palindrome.
#
# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
# Constraints:
#
#     -2^(31) <= x <= 2^(31) - 1
#
#
# Follow up: Could you solve it without converting the integer to a string?
# Я сразу и решаю без конвертации в строку


import math


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    if x == 0:
        return True
    len_x = int(math.log10(x))
    max_d = 10 ** len_x
    min_d = 1
    for _ in range((len_x + 1) // 2):
        if ((x // min_d) % 10) != ((x // max_d) % 10):
            return False
        min_d = min_d * 10
        max_d = max_d / 10
    return True


if __name__ == '__main__':
    tests = {121: True, -121: False, 10: False, 1001: True,
             1000021: False, 100: False, 0: True, 8: True}
    for inp, answer in tests.items():
        print(f'input: {inp}, expected: {answer}, output: {is_palindrome(inp)}')
