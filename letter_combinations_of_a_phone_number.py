# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
# Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.
#
#
#
#
# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
# Example 2:
# Input: digits = ""
# Output: []
#
# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
# Constraints:
#
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].


def letter_combinations(digits: str) -> list[str]:
    dict_letter_digit = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    last_list = []
    for i, digit in enumerate(digits):
        if i == 0:
            last_list = list(dict_letter_digit[digit])
        else:
            new_list = []
            for string in last_list:
                for letter in dict_letter_digit[digit]:
                    new_list.append(string + letter)
            last_list = new_list
    return last_list


if __name__ == '__main__':
    tests = [
        {'digits': '23', 'expected': ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]},
        {'digits': '', 'expected': []},
    ]
    for test in tests:
        answer = letter_combinations(test['digits'])
        print(test, answer)
        print('The answer is correct:', set(test['expected']) == set(answer))
        print('_______')
