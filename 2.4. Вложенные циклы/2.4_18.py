n = int(input())
c = 0
w = 1
m = 0
while c <= n:
    s = 0
    for i in range(w):
        c += 1
        if c <= n:
            s += len(str(c))
        if i < w - 1 and c < n:
            s += 1
    if m < s:
        m = s
    w += 1
c = 0
w = 1
while c <= n:
    st = ''
    for i in range(w):
        c += 1
        if c <= n:
            st += str(c)
        if i < w - 1 and c < n:
            st += ' '
    w += 1
    print(f'{st:^{m}}')
