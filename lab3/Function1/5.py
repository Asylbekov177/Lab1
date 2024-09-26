from itertools import permutations
def permut(string):
    p=permutations(string)
    print(list(p))

a=str(input())
permut(a)
