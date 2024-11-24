from itertools import combinations
n = int(input())
a = [input() for i in range(n)]
for i in combinations(a, 2):
    print(f'{i[0]} - {i[1]}')
