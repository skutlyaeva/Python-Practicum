n = int(input())
a = {}
for i in range(n):
    x = input()
    a[x] = a.get(x, 0) + 1
k = 0
for i in sorted(a):
    if a[i] > 1:
        print(f'{i} - {a[i]}')
    else:
        k = k + 1
if k == n:
    print("Однофамильцев нет")
