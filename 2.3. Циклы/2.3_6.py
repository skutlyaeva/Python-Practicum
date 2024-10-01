a = int(input())
b = int(input())
m = 0
if a > b:
    for i in range(1, b + 1):
        if a % i == 0 and b % i == 0:
            m = max(m, i)
else:
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            m = max(m, i)
print(m)