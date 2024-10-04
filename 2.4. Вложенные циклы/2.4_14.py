a = int(input())
b = int(input())
r = len(str(a * b))
for k in range(a):
    for j in range(b):
        if (k % 2) == 0:
            n = k * b + j + 1
        else:
            n = (k + 1) * b - j
        print(f'{n:>{r}}', end=' ')
    print()
