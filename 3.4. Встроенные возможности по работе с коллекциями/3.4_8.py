n = int(input())
a = [input() for i in range(n)]
m = int(input())
a = a * (m // len(a) + 1)
for i in range(m):
    print(a[i])
