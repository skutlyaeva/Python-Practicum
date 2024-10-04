n = int(input())
l = len(str((n + 1) // 2))
for i in range(n):
    for j in range(n):
        print(f'{min(i + 1, j + 1, n - i, n - j):>{l}}', end=' ')
    print()