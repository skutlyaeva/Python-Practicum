a = int(input())
b = int(input())
r = len(str(a * b))
c = 1
for n in range(a):
    for j in range(b):
        print(f'{c:>{r}}', end=' ')
        c = c + 1
    print()
