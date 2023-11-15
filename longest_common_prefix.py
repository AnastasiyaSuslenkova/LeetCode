# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Constraints:
#
#     1 <= strs.length <= 200
#     0 <= strs[i].length <= 200
#     strs[i] consists of only lowercase English letters.


def longest_common_prefix(strs: list[str]) -> str:
    for i, s in enumerate(strs[0]):
        for string in strs[1:]:
            try:
                if string[i] != s:
                    return string[:i]
            except IndexError:
                return string[:i]
    return strs[0]


if __name__ == '__main__':
    tests = [{'strs': ["flower", "flow", "flight"], 'expected': 'fl'},
             {'strs': ["dog", "racecar", "car"], 'expected': ''},
             {'strs': [''], 'expected': ''},
             {'strs': ['a'], 'expected': 'a'},
             {'strs': ['ab', 'a'], 'expected': 'a'}]
    for test in tests:
        print(test, longest_common_prefix(test['strs']))


