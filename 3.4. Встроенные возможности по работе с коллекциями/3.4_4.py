from itertools import accumulate
for i in accumulate([j + ' ' for j in input().split()]):
    print(i)