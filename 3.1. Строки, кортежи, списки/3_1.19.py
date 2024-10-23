a = a1 = (input()).split()
k = 0
for i in range(len(a1)):
    if a1[i] in '-+*':
        if a[i - k] == '*':
            a[i - k] = str(int(a[i - 2 - k]) * int(a[i - 1 - k]))
            a = a[:i - 2 - k] + a[i - k:]
            k = k + 2
        if a[i - k] == '+':
            a[i - k] = str(int(a[i - 2 - k]) + int(a[i - 1 - k]))
            a = a[:i - 2 - k] + a[i - k:]
            k = k + 2
        if a[i - k] == '-':
            a[i - k] = str(int(a[i - 2 - k]) - int(a[i - 1 - k]))
            a = a[:i - 2 - k] + a[i - k:]
            k = k + 2
print(*a)