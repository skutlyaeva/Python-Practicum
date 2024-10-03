q = int(input())
H = 0
o = 0
err = False
for i in range(q):
    b = int(input())
    h = b % 256
    r = (b // 256) % 256
    m = b // 256 ** 2
    if (37 * (m + r + H)) % 256 != h or (37 * (m + r + H)) % 256 >= 100:
        if err is False:
            o = i
            err = True
    H = h
if err == False:
    print(-1)
else:
    print(o)
