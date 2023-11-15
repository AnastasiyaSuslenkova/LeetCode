# Implement the myAtoi(string s) function,
# which converts a string to a 32-bit signed integer
# (similar to C/C++'s atoi function).
#
# The algorithm for myAtoi(string s) is as follows:
#
# 1. Read in and ignore any leading whitespace.
# 2. Check if the next character (if not already at the end of the string)
# is '-' or '+'. Read this character in if it is either.
# This determines if the final result is negative or positive respectively.
# Assume the result is positive if neither is present.
# 3. Read in next the characters until the next non-digit character
# or the end of the input is reached. The rest of the string is ignored.
# 4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
# If no digits were read, then the integer is 0.
# Change the sign as necessary (from step 2).
# 5. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1],
# then clamp the integer so that it remains in the range.
# Specifically, integers less than -2^31 should be clamped to -2^31,
# and integers greater than 2^31 - 1 should be clamped to 2^31 - 1.
# 6. Return the integer as the final result.
#
# Note:
#     Only the space character ' ' is considered a whitespace character.
#     Do not ignore any characters other than the leading whitespace
#     or the rest of the string after the digits.
#
#
#
# Example 1:
#
# Input: s = "42"
# Output: 42
# Explanation: The underlined characters are what is read in,
# the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "42" ("42" is read in)
#            ^
# The parsed integer is 42.
# Since 42 is in the range [-2^31, 2^31 - 1], the final result is 42.
#
#
# Example 2:
#
# Input: s = "   -42"
# Output: -42
# Explanation:
# Step 1: "   -42" (leading whitespace is read and ignored)
#             ^
# Step 2: "   -42" ('-' is read, so the result should be negative)
#              ^
# Step 3: "   -42" ("42" is read in)
#                ^
# The parsed integer is -42.
# Since -42 is in the range [-2^31, 2^31 - 1], the final result is -42.
#
#
# Example 3:
#
# Input: s = "4193 with words"
# Output: 4193
# Explanation:
# Step 1: "4193 with words" (no characters read because
# there is no leading whitespace)
#          ^
# Step 2: "4193 with words" (no characters read because
# there is neither a '-' nor '+')
#          ^
# Step 3: "4193 with words" ("4193" is read in; reading stops because
# the next character is a non-digit)
#              ^
# The parsed integer is 4193.
# Since 4193 is in the range [-2^31, 2^31 - 1], the final result is 4193.


from itertools import takewhile
import re


def my_atoi(s: str) -> int:
    sgn = 1
    s = s[len(list(takewhile(lambda x: x == ' ', s))):]
    if len(s) == 0:
        return 0
    if s[0] == '-':
        sgn = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    len_num = len(list(takewhile(lambda x: re.match(r'[0-9]', x), s)))
    if len_num == 0:
        return 0
    s = s[:len_num]
    if sgn == -1:
        return max(int(s) * sgn, -2 ** 31)
    return min(int(s) * sgn, 2 ** 31 - 1)


if __name__ == '__main__':
    tests = [{'s': "42", 'expected': 42},
             {'s': "   -42", 'expected': -42},
             {'s': "4193 with words", 'expected': 4193},
             {'s': "-91283472332", 'expected': -2147483648},
             {'s': "", 'expected': 0},
             {'s': "words and 123", 'expected': 0}]
    for test in tests:
        print(test, my_atoi(test['s']))
