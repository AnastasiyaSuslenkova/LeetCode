# Given two strings s and t, return true if t is an anagram of s,
# and false otherwise. An Anagram is a word or phrase formed by rearranging
# the letters of a different word or phrase, typically using all the original
# letters exactly once.
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.


def is_anagram(s: str, t: str) -> bool:
    for letter in set(s + t):
        if s.count(letter) != t.count(letter):
            return False
    return True


if __name__ == '__main__':
    tests = [{'s': 'anagram', 't': 'nagaram', 'expected': True},
             {'s': 'rat', 't': 'car', 'expected': False}]
    for test in tests:
        print(test, is_anagram(test['s'], test['t']))
