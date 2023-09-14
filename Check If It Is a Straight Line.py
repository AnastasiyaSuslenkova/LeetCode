# You are given an array coordinates, coordinates[i] = [x, y],
# where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
#
# Example 1:
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true

# Example 2:
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
#
#
# Constraints:
#
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.

def check_straight_line(coordinates: list[list[int]]) -> bool:
    if len(coordinates) < 3:
        return True
    [x0, y0] = coordinates[0]
    [x1, y1] = coordinates[1]
    if x0 == x1:
        for point in coordinates[2:]:
            if point[0] != x0:
                return False
    else:
        k = (y1 - y0) / (x1 - x0)
        l = y0 - x0 * k
        for point in coordinates[2:]:
            if point[1] != point[0] * k + l:
                return False
    return True

    # можно иначе сделать, запоминаем направляющий вектор (x0, y0) - (x1, y1)
    # который и задает направление нашей прямой
    # и смотрим коллинеарен ли вектор (xi, yi) - (x0, y0) нашему направляющему
    # в этой идее не нужно всякие формулы помнить!
    # на 2 случая делить программу 
    # если входные данные могут быть float наверное проблемы возникнут? но на литкоде вход int по крайней мере


if __name__ == '__main__':
    tests = [{'coordinates': [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]], 'expected': True},
             {'coordinates': [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]], 'expected': False}]
    for test in tests:
        print(test, check_straight_line(test['coordinates']))
