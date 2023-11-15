# Given a string s, find the length of the longest
# substring without repeating characters.
#
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


def length_of_longest_substring(s: str) -> int:
    if len(s) <= 1:
        return len(s)
    in_s = []
    out = 0
    el = s[0]
    for el in s:
        if el in in_s:
            if len(in_s) > out:
                out = len(in_s)
            in_s = in_s[in_s.index(el)+1:]
        in_s.append(el)
    if len(in_s) > out:
        out = len(in_s)
    return out


if __name__ == '__main__':
    tests = {'abcabcbb': 3, 'bbbbb': 1, 'pwwkew': 3, 'au': 2}
    for s, n in tests.items():
        print(f'input: {s}, expected: {n}, output: {length_of_longest_substring(s)}')
