# Given an integer array nums, return true if any value appears
# at least twice in the array, and return false if every element is distinct.
#
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


def contains_duplicate(nums: list[int]) -> bool: # асимптотически супер
    if len(nums) > len(set(nums)):               # выглядит красиво
        return True                              # но, если прям боремся за оптимизацию,
    return False                                 # то можно как только первый дупликат находим
                                                 # возвращать True
                                                 # я бы не стал ниче исправлять :^)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tests = [{'nums': [1, 2, 3, 1], 'expected': True},
             {'nums': [1, 2, 3, 4], 'expected': False},
             {'nums': [1, 1, 1, 3, 3, 4, 3, 2, 4, 2], 'expected': True}]
    for test in tests:
        print(test, contains_duplicate(test['nums']))

