r = -1
H = 1
for i in range(int(input())):
    b = int(input())
    h, r, m = b % 256, (b // 256) % 256, b // 256 ** 2
    t = ((m + r + H) * 37) % 256
    if t != h or h > 99:
        result = i
        break
    hn1 = h
print(result)

