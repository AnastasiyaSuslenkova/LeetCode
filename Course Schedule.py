# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [a_i, b_i] indicates that you must take
# course b_i first if you want to take course a_i.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
#
# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
#
# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
#
#
#
# Constraints:
#
#     1 <= numCourses <= 2000
#     0 <= prerequisites.length <= 5000
#     prerequisites[i].length == 2
#     0 <= a_i, b_i < numCourses
#     All the pairs prerequisites[i] are unique.


import numpy as np


def can_finish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    if not prerequisites:               
        return True
    viewed = []
    prers = np.array(prerequisites)
    firsts = prers[:, 0]
    for prer in prerequisites:       # слабо понимаю что происходит
        if not prer in viewed:       # пытаемся искать циклы что ли
            p = prer                 # еще numCourses нет в теле функции?
            cont = True              #
            sequence = [p[0]]        # хочу сказать, что эта задачка на топологическую сортировку
            while cont:              # т.е. можно формально граф построить 
                viewed.append(p)     # повыкидвать циклы и сравниь оставшееся кол-во вершин с numCourses
                if p[1] in sequence: # это решение, просто я не понимаю пока что, если объяснишь,
                    return False     # то можно детальнее подумать!
                if p[1] in firsts:
                    sequence.append(p[1])
                    p = prerequisites[np.where(firsts == p[1])[0][0]] # эта конструкция ваще пугает
                else:
                    cont = False
    return True


tests = [{'numCourses': 2, 'prerequisites': [[1, 0]], 'expected': True},
         {'numCourses': 2, 'prerequisites': [[1, 0], [0, 1]], 'expected': False},
         {'numCourses': 4, 'prerequisites': [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]], 'expected': False}]
         #                 'prerequisites': [[1, 0], [2, 1], [0, 2]] - цикл длины 3
for test in tests:
    print(test, can_finish(test['numCourses'], test['prerequisites']))
