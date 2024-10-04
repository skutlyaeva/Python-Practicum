n = int(input())
c = 0
for i in range(n):
    x = int(input())
    k = 2
    if x == 1:
        k = 0
    for j in range(2, x // 2 + 1):
        if x % j == 0:
            k = k + 1
    if k == 2:
        c = c + 1
print(c)
