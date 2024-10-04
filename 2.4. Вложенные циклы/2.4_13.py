a = int(input())
b = int(input())
r = len(str(a * b))
n = 1
for k in range(a):
    n = k + 1
    for j in range(b):
        print(f'{n:>{r}}', end=' ')
        n += a
    print()
