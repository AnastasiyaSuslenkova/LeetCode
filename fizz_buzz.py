# Given an integer n, return a string array answer (1-indexed) where:
#
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.


def fizz_buzz(n: int) -> list[str]:
    arr = []
    for i in range(1, n+1):
        if not i % 3:
            if not i % 5:
                arr.append('FizzBuzz')
            else:
                arr.append('Fizz')
        elif not i % 5:
            arr.append('Buzz')
        else:
            arr.append(str(i))
    return arr


if __name__ == '__main__':
    tests = {
        3: ["1", "2", "Fizz"],
        5: ["1", "2", "Fizz", "4", "Buzz"],
        15: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8",
             "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]}
    for inp, expected in tests.items():
        print(f'input: {inp}, \n output: {fizz_buzz(inp)},'
              f'\n expected: {expected} \n \n')
