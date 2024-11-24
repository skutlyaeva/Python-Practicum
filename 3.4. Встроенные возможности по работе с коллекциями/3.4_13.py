from itertools import *
n = int(input())
people = [input() for i in range(n)]
for k in permutations(sorted(people)):
    s = ', '.join(k)
    print(s)