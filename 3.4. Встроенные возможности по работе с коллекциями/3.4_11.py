from itertools import product
a = int(input())
b = int(input())
ln = len(str(a * b))
for i, j in product(range(1, a + 1), range(1, b + 1)):
    print(f'{((i - 1) * b + j):>{ln}}', end=' ')
    if j == b:
        print()
