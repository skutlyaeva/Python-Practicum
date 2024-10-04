n = int(input())
k = 0
for i in range(n):
    x = int(input())
    if x == int(str(x)[::-1]):
        k = k + 1
print(k)