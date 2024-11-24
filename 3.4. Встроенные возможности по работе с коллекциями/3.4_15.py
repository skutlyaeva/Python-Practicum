from itertools import *
n = int(input())
varianti = []
for i in range(n):
    varianti += [x for x in input().split(', ')]
for i in permutations(sorted(varianti), 3):
    j = ' '.join(i)
    print(j)