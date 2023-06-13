#Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four. The same principle applies to the number nine,
# which is written as IX. There are six instances where subtraction is used:

#I can be placed before V (5) and X (10) to make 4 and 9.
#X can be placed before L (50) and C (100) to make 40 and 90.
#C can be placed before D (500) and M (1000) to make 400 and 900.

#Given a roman numeral, convert it to an integer.


def roman_to_int(s: str) -> int:
    integer = 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i, el in enumerate(s):
        if i!=(len(s)-1) and d[el]<d[s[i+1]]:
            integer -= d[el]
        else:
            integer += d[el]
    return integer

if __name__ == '__main__':
    test_roman = {'III': 3, 'LVIII': 58, 'MCMXCIV': 1994}
    for rom in test_roman.keys():
        print(f'input: {rom}, output: {roman_to_int(rom)}, expected: {test_roman[rom]}')
