a = int(input())
p = []
n = 1
if a < 2:
    print(a)
while a > 1:
    n += 1
    if not a % n:
        p.append(str(n))
        a = a // n
        n = 1
else:
    print(' * '.join(p))