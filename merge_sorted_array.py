# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should
# be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
#
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
#
# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
#
# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
#
#
# Constraints:
#
#     nums1.length == m + n
#     nums2.length == n
#     0 <= m, n <= 200
#     1 <= m + n <= 200
#     -10^9 <= nums1[i], nums2[j] <= 10^9


# кривая функция, где все написано вручную, добавляю по одному элементу на нужную позицию
# ниже есть еще одна функция, она сильно лучше
def merge1(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    for i, n2 in enumerate(nums2):
        r = m - 1 + i
        if n2 >= nums1[r]:
            nums1[r + 1] = n2
        elif n2 <= nums1[0]:
            nums1[0:] = [n2] + nums1[:-1] # если убрать [0:], то если возвращать значение,
            # то все ок, но исходный массив при этом не поменяется
        else:
            l = 0
            n1_l = nums1[l]
            while (n1_l != n2) and ((r - l) > 1):
                middle = (l + r) // 2
                if nums1[middle] <= n2:
                    l = middle
                else:
                    r = middle
            nums1[l + 1:] = [n2] + nums1[l + 1:-1]


# потом до меня дошло, что можно было просто сделать вот так:
def merge2(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    nums1[m:] = nums2
    nums1.sort()

# Первый вариант решила оставить, потому что это мне показалось важным.
# Очень показательный пример того, как можно намудрить в простой задаче.
# Зато я сама это заметила. Может, этот случай поможет мне научиться замечать быстрее
# решение типа 2 и не тратить кучу времени на решение типа 1.


if __name__ == '__main__':
    tests = [{'nums1': [1, 2, 3, 0, 0, 0], 'm': 3, 'nums2': [2, 5, 6], 'n': 3, 'expected': [1, 2, 2, 3, 5, 6]},
             {'nums1': [1], 'm': 1, 'nums2': [], 'n': 0, 'expected': [1]},
             {'nums1': [0], 'm': 0, 'nums2': [1], 'n': 1, 'expected': [1]},
             {'nums1': [2, 0], 'm': 1, 'nums2': [1], 'n': 1, 'expected': [1, 2]},
             {'nums1': [4, 5, 6, 0, 0, 0], 'm': 3, 'nums2': [1, 2, 3], 'n': 3, 'expected': [1, 2, 3, 4, 5, 6]}]
    for test in tests:
        print(test)
        merge2(test['nums1'], test['m'], test['nums2'], test['n'])
        print(test['nums1'])
