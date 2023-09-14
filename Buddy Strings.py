# Given two strings s and goal, return true if you can swap two letters
# in s so the result is equal to goal, otherwise, return false.
# Swapping letters is defined as taking two indices i and j (0-indexed)
# such that i != j and swapping the characters at s[i] and s[j].
# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
#
# Example 1:
# Input: s = "ab", goal = "ba"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
#
# Example 2:
# Input: s = "ab", goal = "ab"
# Output: false
# Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
#
# Example 3:
# Input: s = "aa", goal = "aa"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
#
#
# Constraints:
#     1 <= s.length, goal.length <= 2 * 10^4
#     s and goal consist of lowercase letters.


def buddy_strings(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    diff_i = []
    i = 0
    while (i < len(s)) and (len(diff_i) < 3): # можно попробовать так: (не уверен, что это будет лучше)
        if s[i] != goal[i]:                   # for i, (letter1, letter2)  in enumerate(zip(s, goal)):
            diff_i.append(i)                  #     if letter1 != letter2:
        i += 1                                #         diff_i.append(i)
                                              #     if len(diff_i) > 2:
                                              #         break
                                              # теперь не обращаемся к буквам по индексам!

    if len(diff_i) == 0:
        if len(s) > len(set(s)):              # создание множества уникальных букв в s
            return True                       # можно в верхний цикл поместить
        else:                                 # 
            return False                      # чтоб создать set(s), нам же еще раз придется пробежаться 
                                              # по s, не очень хорошо, но не знаю как сделать лучше
    if len(diff_i) == 2:
        if (s[diff_i[0]] == goal[diff_i[1]]) and (s[diff_i[1]] == goal[diff_i[0]]):
            return True
    return False


tests = [{'s': 'ab', 'goal': 'ba', 'expected': True},
         {'s': 'ab', 'goal': 'ab', 'expected': False},
         {'s': 'aa', 'goal': 'aa', 'expected': True},
         {'s': 'aaaaaaaaaaaaaaaaaaaaaa', 'goal': 'aaaaaaaaaaaaaaaaaaaaaa', 'expected': True}]

         # 's': 'a' 'goal': 'a'
         
for test in tests:
    print(test, buddy_strings(test['s'], test['goal']))
