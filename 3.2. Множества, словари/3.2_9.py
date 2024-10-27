a = {}
while (x := input()) != '':
    s = x.split()
    for i in s:
        if i in a:
            a[i] = a[i] + 1
        else:
            a[i] = 1
for i in a:
    print(i, a[i])
