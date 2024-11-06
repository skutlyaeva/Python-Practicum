n = int(input())
a = {}
for i in range(n):
    x = input()
    a[x] = a.get(x, 0) + 1
k = 0
for i in a:
    if a[i] > 1:
        k = k + a[i]
print(k)