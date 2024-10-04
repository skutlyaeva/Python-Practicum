n = int(input())
s = 0
b = 0
for i in range(10, 1, -1):
    summ = 0
    num = n
    while num > 0:
        summ += (num % i)
        num = num // i
    if summ >= s:
        s = summ
        b = i
print(b)
