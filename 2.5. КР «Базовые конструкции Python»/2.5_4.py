n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
M = min(a)
for i in range(1, len(a)):
    if a[i] < a[i - 1]:
        M = max(M, a[i])
print(M)
