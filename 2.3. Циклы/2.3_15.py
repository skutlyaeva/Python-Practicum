a = int(input())
k = 0
while a != 0:
    s = input()
    if 'зайка' in s:
        k = k + 1
    a = a - 1
print(k)