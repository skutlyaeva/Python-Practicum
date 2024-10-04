a = int(input())
b = int(input())
r = len(str(a * b))
for k in range(a):
    for j in range(b):
        if (j % 2) == 0:
            n = j * a + k + 1
        else:
            n = (j + 1) * a - k
        print(f'{n:>{r}}', end=' ')
    print()