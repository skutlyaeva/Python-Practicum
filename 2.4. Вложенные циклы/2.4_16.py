a = int(input())
b = int(input())
l = a * b + (a - 1)
for i in range(a):
    for j in range(a):
        print(f'{((i + 1) * (j + 1)): ^{b}}', end='')
        if j == a - 1:
            print()
        else:
            print('|', end='')
    if i + 1 != a:
        print('-' * l)