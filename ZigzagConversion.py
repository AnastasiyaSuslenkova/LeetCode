# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
#
#
#
# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"
#
#
#
# Constraints:
#     1 <= s.length <= 1000
#     s consists of English letters (lower-case and upper-case), ',' and '.'.
#     1 <= numRows <= 1000


def convert(s: str, num_rows: int) -> str:
    if num_rows == 1:
        return s
    words = [str() for i in range(num_rows)]
    for i, s_i in enumerate(s):
        diff_pos = 2 * num_rows - 2
        ost = i % diff_pos
        if ost < num_rows:
            words[ost] = words[ost] + s_i # строка неизменяемый объект, поэтому
                                          # эта операция создает новую строку формально,
                                          # а это по времени работает за длину строки.
                                          # если пользоваться +=, будет быстрее, потому что 
                                          # питон выделяет память как раз на эту операцию, 
                                          # так что, если мы не сильно удлиняем строчку, то 
                                          # эта операция работает за константу
                                          #
                                          # я бы делал так:
                                          #
                                          # words = [[] for i in range(num_rows)]
                                          # words[ost].apped('s_i')
                                          #
                                          # на всякий случай
        else:
            pos = diff_pos - ost
            words[pos] = words[pos] + s_i
    return "".join(words)


if __name__ == '__main__':
    tests = [{'s': "PAYPALISHIRING", 'num_rows': 3, 'expected': "PAHNAPLSIIGYIR"},
             {'s': "PAYPALISHIRING", 'num_rows': 4, 'expected': "PINALSIGYAHRPI"},
             {'s': "A", 'num_rows': 1, 'expected': "A"}]
    for test in tests:
        print(test, convert(test['s'], test['num_rows']))
