def gcd(*s):
    a = list(s)
    while len(a) > 1:
        while a[1]:
            a[0], a[1] = a[1], a[0] % a[1]
        a.pop(1)
    return a[0]