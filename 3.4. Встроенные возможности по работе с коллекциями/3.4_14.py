from itertools import *
n = int(input())
names = [input() for i in range(n)]
for i in permutations(sorted(names), 3):
    j = ', '.join(i)
    print(j)
