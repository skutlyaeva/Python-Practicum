n = int(input())
s = ' '
c1 = (n % 10) + (n // 10 % 10)
c2 = (n // 10 % 10) + (n // 100)
if c1 > c2:
    s = str(c1) + str(c2)
else:
    s = str(c2) + str(c1)
print(int(s))