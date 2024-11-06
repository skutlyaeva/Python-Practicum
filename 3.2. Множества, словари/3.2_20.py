s = set(input().split('; '))
n = []
for i in s:
    n.append(int(i))
n.sort()
for i in n:
    r = []
    for j in n:
        if i != j:
            a, b = i, j
            while b != 0:
                a, b = b, a % b
            if a == 1:
                r.append(str(j))
    if r:
        print(i, '-', ", ".join(r))