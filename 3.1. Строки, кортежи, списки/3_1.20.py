from math import factorial
a = a1 = (input()).split()
k = 0
for i in range(len(a1)):
    if a1[i] in '+-*~/!#@':
        if a[i - k] == '*':
            a[i - k] = str(int(a[i - 2 - k]) * int(a[i - 1 - k]))
            a = a[:i - 2 - k] + a[i - k:]
            k += 2
        elif a[i - k] == '-':
            a[i - k] = str(int(a[i - 2 - k]) - int(a[i - 1 - k]))
            a = a[:i - 2 - k] + a[i - k:]
            k += 2
        elif a[i - k] == '+':
            a[i - k] = str(int(a[i - 2 - k]) + int(a[i - 1 - k]))
            a = a[:i - 2 - k] + a[i - k:]
            k += 2
        elif a[i - k] == '/':
            a[i - k] = str(int(a[i - 2 - k]) // int(a[i - 1 - k]))
            a = a[:i - 2 - k] + a[i - k:]
            k += 2
        elif a[i - k] == '~':
            a[i - k] = str(int(a[i - 1 - k]) * (-1))
            a = a[:i - 1 - k] + a[i - k:]
            k += 1
        elif a[i - k] == '!':
            a[i - k] = str(factorial(int(a[i - 1 - k])))
            a = a[:i - 1 - k] + a[i - k:]
            k += 1
        elif a[i - k] == '#':
            a[i - k] = a[i - 1 - k]
        elif a[i - k] == '@':
            a[i - k - 3], a[i - k - 2], a[i - k - 1] = a[i - k - 2], a[i - k - 1], a[i - k - 3]
            a = a[:i - k] + a[i + 1 - k:]
            k += 1
    else:
        ...
print(*a)
