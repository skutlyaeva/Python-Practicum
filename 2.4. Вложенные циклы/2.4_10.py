n = int(input())
print('А Б В')
for i in range(1, n):
    for j in range(1, n):
        for e in range(1, n):
            if (i + j + e) == n:
                print(i, j, e)
