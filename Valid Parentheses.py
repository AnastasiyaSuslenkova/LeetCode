# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.
#
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "[()]"
# Output: true

def is_valid(s: str) -> bool:
    dict_of_brackets = {'{': '}', '(': ')', '[': ']'}
    l_opened = []
    for i, el in enumerate(s):
        if el in dict_of_brackets.keys():
            l_opened.append(dict_of_brackets[el])
        elif len(l_opened) == 0:
            return False
        elif el == l_opened[-1]:
            l_opened = l_opened[:-1]
        else:
            return False
    if len(l_opened) > 0:
        return False
    return True


if __name__ == '__main__':
    tests = {'()': True, '()[]{}': True, '(]': False, '[()]': True}
    for input, expected in tests.items():
        print(input, is_valid(input), expected)
