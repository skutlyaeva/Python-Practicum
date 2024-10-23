n = int(input())
k = 0
for i in range(n):
    x = input()
    k = k + x.count('зайка')
print(k)