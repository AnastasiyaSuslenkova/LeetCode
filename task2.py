# Given two strings ransomNote and magazine,
# return true if ransomNote can be constructed
# by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.

def can_construct(ransom_note: str, magazine: str) -> bool:
    for s in set(ransom_note):
        if magazine.count(s) < ransom_note.count(s):
            return False
    return True


r_n, mag = 'ransom_note', 'magazine'
tests = [{r_n: 'a', mag: 'b', 'exp_answer': False},
         {r_n: 'aa', mag: 'ab', 'exp_answer': False},
         {r_n: 'aa', mag: 'aab', 'exp_answer': True}]
for test in tests:
    print(f'{test}, output: {can_construct(test[r_n], test[mag])}')
