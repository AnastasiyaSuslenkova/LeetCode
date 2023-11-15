# Given an integer num, return the number of steps to reduce it to zero.
# In one step, if the current number is even, you have to divide it by 2,
# otherwise, you have to subtract 1 from it.

def number_of_steps(num: int) -> int:
    num_steps = 0
    while num > 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num -= 1
        num_steps += 1
    return num_steps


if __name__ == '__main__':
    tests = {14: 6, 8: 4, 123: 12}
    for inp, expected in tests.items():
        print(f'input: {inp}, expected: {expected}, output: {number_of_steps(inp)}')
