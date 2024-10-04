n = int(input())
k = 0
c = 0
for i in range(n):
    while (x := input()) != 'ВСЁ':
        if x == 'зайка':
            k = k + 1
    if k > 0:
        c = c + 1
        k = 0
print(c)
