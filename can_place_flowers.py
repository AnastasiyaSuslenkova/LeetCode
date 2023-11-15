# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's,
# where 0 means empty and 1 means not empty,
# and an integer n, return true if n new flowers can be planted in the flowerbed
# without violating the no-adjacent-flowers rule and false otherwise.
#
#
#
# Example 1:
#
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
#
# Example 2:
#
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
#
#
#
# Constraints:
#
#     1 <= flowerbed.length <= 2 * 10^4
#     flowerbed[i] is 0 or 1.
#     There are no two adjacent flowers in flowerbed.
#     0 <= n <= flowerbed.length


def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    if n == 0:
        return True
    n_places = 0
    for i, place in enumerate(flowerbed):
        if place == 1:
            continue
        if (i == 0) or (flowerbed[i - 1] == 0):
            if (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0):
                n_places += 1
                flowerbed[i] = 1
        if n_places == n:
            return True
    return False


if __name__ == '__main__':
    tests = [{'flowerbed': [1, 0, 0, 0, 1], 'n': 1, 'expected': True},
             {'flowerbed': [1, 0, 0, 0, 1], 'n': 2, 'expected': False},
             {'flowerbed': [1, 0, 0, 0, 0, 1], 'n': 2, 'expected': False},
             {'flowerbed': [1, 0, 0, 0, 1, 0, 0], 'n': 2, 'expected': True},
             {'flowerbed': [1, 0, 0, 0, 0, 0, 1], 'n': 2, 'expected': True}]
    for test in tests:
        print(test, can_place_flowers(test['flowerbed'], test['n']))
