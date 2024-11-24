n = int(input())
print(f'А Б В')
for a in range(1, n + 1):
    for b in range(1, n + 1 - a):
        for v in range(1, n + 1 - a - b):
            if (a + b + v) == n:
                print(f'{a} {b} {v}')
