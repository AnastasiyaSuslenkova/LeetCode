# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply
# X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
# Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same
# principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
#     I can be placed before V (5) and X (10) to make 4 and 9.
#     X can be placed before L (50) and C (100) to make 40 and 90.
#     C can be placed before D (500) and M (1000) to make 400 and 900.
#
# Given an integer, convert it to a roman numeral.
#
#
#
# Example 1:
#
# Input: num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones.
#
# Example 2:
#
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
#
# Example 3:
#
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#
#
# Constraints:
#
#     1 <= num <= 3999


def int_to_roman(num: int) -> str:
    dict_roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    roman_keys_sorted = [1000, 100, 10, 1]
    num_ost = num
    s = ''
    for i, k in enumerate(roman_keys_sorted):
        n = num_ost // k
        num_ost -= n * k
        if i == 0:
            s += dict_roman[k] * n
        else:
            if n == 4:
                s += dict_roman[k] + dict_roman[k * 5]
            elif n == 9:
                s += dict_roman[k] + dict_roman[k * 10]
            else:
                if n >= 5:
                    s += dict_roman[k * 5]
                    n -= 5
                s += dict_roman[k] * n
    return s


if __name__ == '__main__':
    tests = [{'num': 3, 'expected': 'III'},
             {'num': 58, 'expected': 'LVIII'},
             {'num': 1994, 'expected': 'MCMXCIV'}]
    for test in tests:
        print(test, int_to_roman(test['num']))