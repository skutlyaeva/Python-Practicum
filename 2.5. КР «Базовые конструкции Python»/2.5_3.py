m = int(input())
n = int(input())
k = (n - m) % 10
a = []
while n <= m:
    a.append(n)
    n = n + k
b = ', '.join(map(str, a))
print(b)
